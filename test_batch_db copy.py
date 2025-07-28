import mysql.connector
from mysql.connector import Error
from item_processor import ItemProcessor

from item_reader import ItemReader
from item_writer import ItemWriter
from job import Job
from job_launcher import JobLauncher
from step import Step


class YourConcreteItemReader(ItemReader):
    def read(self, fetch_size):
        # Connect to the database and read data from the product table
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  # Add your MySQL password here if required
                database="SpringDB"
            )
            if connection.is_connected():
                cursor = connection.cursor(dictionary=True)  # Fetch data as dictionaries
                cursor.execute("SELECT * FROM product")
                data = [row for row in cursor.fetchall()]
                cursor.close()
                connection.close()
                return data
        except Error as e:
            print("Error reading data from MySQL table:", e)
        return []


class YourConcreteItemProcessor(ItemProcessor):
    def process(self, item):
        # Update the price of the product by adding 1
        item['price'] += 1
        return item

class YourConcreteItemWriter(ItemWriter):
    def write(self, items):
        # Connect to the database and update the prices in the product table
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  # Add your MySQL password here if required
                database="SpringDB"
            )
            if connection.is_connected():
                cursor = connection.cursor()
                for item in items:
                    cursor.execute("UPDATE product SET price = %s WHERE id = %s", (item['price'], item['id']))
                connection.commit()
                cursor.close()
                connection.close()
                print("Prices updated successfully.")
        except Error as e:
            print("Error updating prices in MySQL table:", e)

if __name__ == "__main__":
    # Define concrete implementations for ItemReader, ItemProcessor, and ItemWriter
    concrete_reader = YourConcreteItemReader()
    concrete_processor = YourConcreteItemProcessor()
    concrete_writer = YourConcreteItemWriter()

    # Create a Step with the concrete components
    step = Step(reader=concrete_reader, processor=concrete_processor, writer=concrete_writer)

    # Create a Job with the Step and job configuration
 # Create a JobLauncher and launch the Job
    job = Job(steps=[step], retry_limit=3, skip_limit=10, fetch_size=100)

    job_launcher = JobLauncher()
    job_launcher.launch(job)
