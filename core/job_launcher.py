# core/job_launcher.py

import mysql.connector
from mysql.connector import Error
from core.metadata_manager import MetadataManager

class JobLauncher:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def launch(self, job):
        # Create metadata tables if they do not exist
        metadata_manager = MetadataManager(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        metadata_manager.create_metadata_tables()

        # Launch the job
        job.execute()
