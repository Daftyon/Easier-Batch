# core/job.py

import mysql.connector
from mysql.connector import Error
from core.metadata_manager import MetadataManager

class Job:
    def __init__(self, steps, retry_limit=3, skip_limit=10, fetch_size=100, parallel=False):
        self.steps = steps
        self.retry_limit = retry_limit
        self.skip_limit = skip_limit
        self.fetch_size = fetch_size
        self.parallel = parallel
        self.job_id = None  # To store the job ID obtained from the metadata table

    def execute(self):
        # Update job metadata with status 'running'
        self.update_job_metadata(status='running')

        # Execute steps
        for step in self.steps:
            # Update step metadata with status 'running'
            step_id = self.update_step_metadata(step_name=step.name, status='running')

            retry_count = 0
            skip_count = 0
            while retry_count < self.retry_limit:
                try:
                    step.execute(self.fetch_size)
                    # Update step metadata with status 'completed'
                    self.update_step_metadata(step_id, status='completed')
                    break
                except Exception as e:
                    # Handle errors and retries
                    retry_count += 1
                    # Log retry attempts

        # Update job metadata with status 'completed'
        self.update_job_metadata(status='completed')

    def update_job_metadata(self, status):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  # Add your MySQL password here if required
                database="SpringDB"
            )
            if connection.is_connected():
                cursor = connection.cursor()
                # Update job metadata table
                cursor.execute("UPDATE job_metadata SET status = %s WHERE job_id = %s", (status, self.job_id))
                connection.commit()
        except Error as e:
            print("Error updating job metadata:", e)
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

    def update_step_metadata(self, step_id, status):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  # Add your MySQL password here if required
                database="SpringDB"
            )
            if connection.is_connected():
                cursor = connection.cursor()
                # Update step metadata table
                cursor.execute("UPDATE step_metadata SET status = %s WHERE step_id = %s", (status, step_id))
                connection.commit()
        except Error as e:
            print("Error updating step metadata:", e)
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()
