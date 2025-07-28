# core/metadata_manager.py

import mysql.connector
from mysql.connector import Error

class MetadataManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def create_metadata_tables(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if connection.is_connected():
                cursor = connection.cursor()
                # Create Job Metadata Table if not exists
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS job_metadata (
                        job_id INT AUTO_INCREMENT PRIMARY KEY,
                        job_name VARCHAR(255) NOT NULL,
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                        status VARCHAR(50)
                    )
                """)

                # Create Step Metadata Table if not exists
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS step_metadata (
                        step_id INT AUTO_INCREMENT PRIMARY KEY,
                        job_id INT,
                        step_name VARCHAR(255) NOT NULL,
                        status VARCHAR(50),
                        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                        completed_at DATETIME,
                        FOREIGN KEY (job_id) REFERENCES job_metadata(job_id)
                    )
                """)
                connection.commit()
                print("Metadata tables created successfully.")
        except Error as e:
            print("Error creating metadata tables:", e)
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

# Usage example:
if __name__ == "__main__":
    # Update with your MySQL connection details
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DATABASE = "SpringDB"

    # Create an instance of MetadataManager
    metadata_manager = MetadataManager(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )

    # Create metadata tables if they do not exist
    metadata_manager.create_metadata_tables()
