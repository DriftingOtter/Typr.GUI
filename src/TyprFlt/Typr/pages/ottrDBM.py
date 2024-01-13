import uuid
import mysql.connector
from mysql.connector import Error as MySQLError, errorcode
import hashlib
import logging
import re
import datetime


class OttrDBM:
    def __init__(self, dbConfig):
        self.config = dbConfig
        self.connection = None

    def connect_to_database(self):
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

    def create_user_table(self, cursor):
        # Create the users table if not exists
        create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                uid VARCHAR(36),
                email VARCHAR(255) UNIQUE,
                password VARCHAR(255)
            )
        """
        cursor.execute(create_table_query)

    def is_valid_email(self, email):
        pattern = r"[^@]+@[^@]+\.[^@]+$"
        return re.match(pattern, email) is not None

    def is_strong_password(self, password):
        if len(password) < 8:
            return False

        has_capital_letter = False
        has_number = False
        has_special_character = False

        for char in password:
            if char.isupper():
                has_capital_letter = True
            elif char.isdigit():
                has_number = True
            elif not char.isalnum():
                has_special_character = True

        return has_capital_letter and has_number and has_special_character

    def create_user(self, email, password):
        if not self.is_valid_email(email):
            logging.error(
                "Error: Invalid email format. Please provide a valid email address."
            )
            return 1  # Error code for invalid email format

        if not self.is_strong_password(password):
            logging.error(
                "Error: Weak password. Please use a password with at least 8 characters, one capital letter, one number, and one special character."
            )
            return 2  # Error code for weak password

        connection = self.connect_to_database()
        if not connection:
            return 3  # Error code for database connection failure

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
                if cursor.fetchone():
                    logging.info("Email already exists. Please choose a different one.")
                    return 4  # Error code for email already exists

                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                user_id = str(uuid.uuid4())

                cursor.execute(
                    "INSERT INTO users (uid, email, password) VALUES (%s, %s, %s)",
                    (user_id, email, hashed_password),
                )

            connection.commit()

            logging.info(
                "User with email %s successfully created. UID: %s", email, user_id
            )
            return 0, user_id  # Success

        except Exception as e:
            logging.error("An error occurred during user creation: %s", str(e))
            return 5  # Error code for other exceptions

        finally:
            if connection:
                connection.close()

    def authenticate_user(self, email, password):
        if not self.is_valid_email(email):
            logging.error(
                "Error: Invalid email format. Please provide a valid email address."
            )
            return 1  # Error code for invalid email format

        connection = self.connect_to_database()
        if not connection:
            return 2  # Error code for database connection failure

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT password, uid FROM users WHERE email = %s", (email,)
                )
                user_data = cursor.fetchone()

                if user_data:
                    hashed_password, user_id = user_data
                    entered_password_hash = hashlib.sha256(password.encode()).hexdigest()

                    if entered_password_hash == hashed_password:
                        logging.info("Login successful. UID: %s", user_id)

                        return 0, user_id  # Success

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

    def add_test_score(self, user_id, wpm, acc, ttk, test_type, date):
        connection = self.connect_to_database()
        if not connection:
            return 6  # Error code for database connection failure

        try:
            with connection.cursor() as cursor:
                # Insert the new test score record
                cursor.execute(
                    "INSERT INTO users_scores (uid, wpm, acc, ttk, test_type, date) VALUES (%s, %s, %s, %s, %s, %s)",
                    (user_id, wpm, acc, ttk, test_type, date),
                )

            connection.commit()

            logging.info("Test score successfully added for user %s.", user_id)
            return 0  # Success

        except Exception as e:
            logging.error("An error occurred during test score addition: %s", str(e))
            return 7  # Error code for other exceptions

        finally:
            if connection:
                connection.close()

    def find_personal_best(self, user_id):
        connection = self.connect_to_database()
        if not connection:
            return None  # Return None for database connection failure

        try:
            with connection.cursor() as cursor:
                # Query the database to find the greatest WPM, ACC, and TTK scores for the given UID
                cursor.execute(
                    "SELECT MAX(wpm), MAX(acc), MAX(ttk) FROM users_scores WHERE uid = %s",
                    (user_id,),
                )
                personal_best = cursor.fetchone()

                if personal_best and any(value is not None for value in personal_best):
                    logging.info(
                        "Personal best scores for user %s: WPM: %s, ACC: %s, TTK: %s",
                        user_id,
                        personal_best[0],
                        personal_best[1],
                        personal_best[2],
                    )
                    return personal_best  # Return the personal best WPM, ACC, and TTK scores

                logging.info("No test scores found for user %s", user_id)
                return None  # Return None if no test scores found for the given UID

        except Exception as e:
            logging.error(
                "An error occurred while finding personal best scores: %s", str(e)
            )
            return None  # Return None for other exceptions

        finally:
            if connection:
                connection.close()

    def find_total_time_played(self, user_id):
        connection = self.connect_to_database()
        if not connection:
            return None  # Return None for database connection failure

        try:
            with connection.cursor() as cursor:
                # Query the database to find the total time played for the given UID
                cursor.execute(
                    "SELECT SUM(ttk) FROM users_scores WHERE uid = %s", (user_id,)
                )
                total_time_seconds = cursor.fetchone()[0]

                if total_time_seconds is not None:
                    # Convert total time from seconds to hours:minutes:seconds format
                    total_time_formatted = str(
                        datetime.timedelta(seconds=int(total_time_seconds))
                    )
                    logging.info(
                        "Total time played for user %s: %s", user_id, total_time_formatted
                    )
                    return total_time_formatted  # Return the total time played

                logging.info("No test scores found for user %s", user_id)
                return None  # Return None if no test scores found for the given UID

        except Exception as e:
            logging.error(
                "An error occurred while finding total time played: %s", str(e)
            )
            return None  # Return None for other exceptions

        finally:
            if connection:
                connection.close()

    def fetch_data_for_plot(self, metric, user_id):
        connection = self.connect_to_database()
        if not connection:
            return None  # Return None for database connection failure

        try:
            with connection.cursor(dictionary=True) as cursor:
                # Query the database to fetch the specified metric (WPM, ACC, or TTK) for a given UID
                cursor.execute(
                    f"SELECT date, {metric} FROM users_scores WHERE uid = %s", (user_id,)
                )
                data = cursor.fetchall()

                return data

        except Exception as e:
            logging.error(
                f"An error occurred while fetching data for {metric}: {str(e)}"
            )
            return None  # Return None for other exceptions

        finally:
            if connection:
                connection.close()

