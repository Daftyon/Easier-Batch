from batch import ItemProcessor, ItemReader, ItemWriter, Job, JobLauncher, Step

class YourConcreteItemReader(ItemReader):
    def read(self, fetch_size):
        try:
            with open('your_data_file.txt', 'r') as file:
                data = [line.strip() for line in file]
        except FileNotFoundError:
            data = []
        return data

class YourConcreteItemProcessor(ItemProcessor):
    def process(self, item):
        # Replace names containing 'A' with names containing 'X'
        processed_item = item.replace('x', 'A')
        print("processed_item 1 :",processed_item)
        processed_item = processed_item.replace('x', 'a')
        print("processed_item 2 :",processed_item)

        return processed_item

class YourConcreteItemWriter(ItemWriter):
    def write(self, items):
        # Implement the logic to write processed items to a destination
        # In this case, write the updated names back to the file
        with open('your_data_file.txt', 'w') as file:
            for item in items:
                file.write(item + '\n')
if __name__ == "__main__":
    # Configure logging format
    # logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Define concrete implementations for ItemReader, ItemProcessor, and ItemWriter
    concrete_reader = YourConcreteItemReader()
    concrete_processor = YourConcreteItemProcessor()
    concrete_writer = YourConcreteItemWriter()

    # Create a Step with the concrete components
    step = Step(reader=concrete_reader, processor=concrete_processor, writer=concrete_writer)

    # Create a Job with the Step and job configuration parameters
    job = Job(steps=[step], retry_limit=3, skip_limit=10, fetch_size=100)

    # Create a JobLauncher and launch the Job
    job_launcher = JobLauncher()
    job_launcher.launch(job)
