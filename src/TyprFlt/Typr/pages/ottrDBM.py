import uuid
import mysql.connector
from mysql.connector import Error as MySQLError, errorcode
import hashlib
import logging
import re


class OttrDBM:
    def __init__(self, dbConfig):
        self.config = dbConfig
        self.connection = None

    def connectToDatabase(self):
        try:
            # Connect to MariaDB
            self.connection = mysql.connector.connect(**self.config)
            return self.connection
        except MySQLError as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.error("Error: Invalid MariaDB credentials. %s", err)
            else:
                logging.error("Error: %s", err)
            return None

    def createUserTable(self, cursor):
        # Create the users table if not exists
        createTableQuery = """
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                uid VARCHAR(36),
                email VARCHAR(255) UNIQUE,
                password VARCHAR(255)
            )
        """
        cursor.execute(createTableQuery)

    def createOrUpdateUserTable(self, cursor, dbName):
        # Replace hyphens with underscores in the table name
        sanitizedDbName = dbName.replace("-", "_")

        # Check if 'users' table exists before creating the foreign key
        cursor.execute("SHOW TABLES LIKE 'users'")
        if cursor.fetchone():
            createTableQuery = f"""
                CREATE TABLE IF NOT EXISTS {sanitizedDbName} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    uid VARCHAR(36),
                    wpm INT,
                    acc INT,
                    ttk INT,
                    testName VARCHAR(4),
                    FOREIGN KEY (uid) REFERENCES users(uid)
                )
            """
            cursor.execute(createTableQuery)
        else:
            logging.error("Error: 'users' table does not exist.")

    def isValidEmail(self, email):
        pattern = r"[^@]+@[^@]+\.[^@]+$"
        return re.match(pattern, email) is not None

    def isStrongPassword(self, password):
        if len(password) < 8:
            return False

        hasCapitalLetter = False
        hasNumber = False
        hasSpecialCharacter = False

        for char in password:
            if char.isupper():
                hasCapitalLetter = True
            elif char.isdigit():
                hasNumber = True
            elif not char.isalnum():
                hasSpecialCharacter = True

        return hasCapitalLetter and hasNumber and hasSpecialCharacter

    def createUser(self, email, password):
        if not self.isValidEmail(email):
            logging.error(
                "Error: Invalid email format. Please provide a valid email address."
            )
            return 1  # Error code for invalid email format

        if not self.isStrongPassword(password):
            logging.error(
                "Error: Weak password. Please use a password with at least 8 characters, one capital letter, one number, and one special character."
            )
            return 2  # Error code for weak password

        connection = self.connectToDatabase()
        if not connection:
            return 3  # Error code for database connection failure

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
                if cursor.fetchone():
                    logging.info("Email already exists. Please choose a different one.")
                    return 4  # Error code for email already exists

                hashedPassword = hashlib.sha256(password.encode()).hexdigest()
                userId = str(uuid.uuid4())

                cursor.execute(
                    "INSERT INTO users (uid, email, password) VALUES (%s, %s, %s)",
                    (userId, email, hashedPassword),
                )

                self.createOrUpdateUserTable(cursor, f"user_{userId}")

            connection.commit()

            logging.info(
                "User with email %s successfully created. UID: %s", email, userId
            )
            return 0  # Success

        except Exception as e:
            logging.error("An error occurred during user creation: %s", str(e))
            return 5  # Error code for other exceptions

        finally:
            if connection:
                connection.close()

    def authenticateUser(self, email, password):
        if not self.isValidEmail(email):
            logging.error(
                "Error: Invalid email format. Please provide a valid email address."
            )
            return 1  # Error code for invalid email format

        connection = self.connectToDatabase()
        if not connection:
            return 2  # Error code for database connection failure

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT password, uid FROM users WHERE email = %s", (email,)
                )
                userData = cursor.fetchone()

                if userData:
                    hashedPassword, userId = userData
                    enteredPasswordHash = hashlib.sha256(password.encode()).hexdigest()

                    if enteredPasswordHash == hashedPassword:
                        logging.info("Login successful. UID: %s", userId)

                        userDbName = f"user_{userId}"

                        # Check if the user's dedicated table exists, create if not
                        self.createOrUpdateUserTable(cursor, userDbName)

                        # Connect to the user's dedicated database
                        userConfig = {**self.config, "database": userDbName}
                        with mysql.connector.connect(
                            **userConfig
                        ) as userConnection, userConnection.cursor() as userCursor:
                            logging.info(
                                "Connected to the database for user %s.", email
                            )

                            # Perform operations specific to the authenticated user's database
                            # For example: userCursor.execute("CREATE TABLE IF NOT EXISTS ...")

                        return 0  # Success

                    else:
                        logging.error("Error: Invalid email or password.")
                        return 3  # Error code for invalid email or password

                else:
                    logging.info("User not found.")
                    return 4  # Error code for user not found

        except Exception as e:
            logging.error("An error occurred during user authentication: %s", str(e))
            return 5  # Error code for other exceptions

        finally:
            if connection:
                connection.close()


# Example Usage:
# db_manager = OttrDBM({
#     'user': 'your_username',
#     'password': 'your_password',
#     'host': 'your_host',
#     'database': 'your_database'
# })
#
# result = db_manager.createUser('user@example.com', 'P@ssw0rd')
#
# if result == 0:
#     print("User creation successful!")
# elif result == 1:
#     print("Invalid email format. Please provide a valid email address.")
# elif result == 2:
#     print("Weak password. Please use a stronger password.")
# elif result == 3:
#     print("Database connection failure.")
# elif result == 4:
#     print("Email already exists.")
#
# result = db_manager.authenticateUser('user@example.com', 'P@ssw0rd')
#
# if result == 0:
#     print("Login successful!")
# elif result == 1:
#     print("Invalid email format. Please provide a valid email address.")
# elif result == 2:
#     print("Database connection failure.")
# elif result == 3:
#     print("Invalid email or password.")
# elif result == 4:
#     print("User not found.")
