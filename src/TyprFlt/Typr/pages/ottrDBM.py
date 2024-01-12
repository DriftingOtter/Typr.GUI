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

            connection.commit()

            # Create the user's test scores table
            self.createTestScoresTable(cursor, email)

            logging.info(
                "User with email %s successfully created. UID: %s", email, userId
            )
            return 0, userId  # Success

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

                        return 0, userId  # Success

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

    def addTestScore(self, uid, wpm, acc, ttk, test_type):
        connection = self.connectToDatabase()
        if not connection:
            return 6  # Error code for database connection failure

        try:
            with connection.cursor() as cursor:
                # Insert the new test score record
                cursor.execute(
                    "INSERT INTO users_scores (uid, wpm, acc, ttk, test_type) VALUES (%s, %s, %s, %s, %s)",
                    (uid, wpm, acc, ttk, test_type),
                )

            connection.commit()

            logging.info("Test score successfully added for user %s.", uid)
            return 0  # Success

        except Exception as e:
            logging.error("An error occurred during test score addition: %s", str(e))
            return 7  # Error code for other exceptions

        finally:
            if connection:
                connection.close()


# Example usage:
# db_config = {
#     "host": "your_host",
#     "user": "your_user",
#     "password": "your_password",
#     "database": "your_database"
# }
# ottr_dbm = OttrDBM(db_config)
# ottr_dbm.createTestScoresTable(cursor, "example@email.com")
# result = ottr_dbm.addTestScore("example@email.com", 100, 95, 30, "A")
# print(result)
