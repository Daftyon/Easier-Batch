import logging
import time
import threading

# Configure logging
logging.basicConfig(filename='batch_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ItemReader:
    def read(self, fetch_size):
        # Read data from a source (e.g., database, file, API) with the specified fetch size
        # Return data in chunks
        pass

class ItemProcessor:
    def process(self, item):
        # Apply business logic to process each item
        return item

class ItemWriter:
    def write(self, items):
        # Write processed items to a destination (e.g., database, file, API)
        pass

class Step:
    def __init__(self, reader, processor, writer):
        self.reader = reader
        self.processor = processor
        self.writer = writer

    def execute(self, fetch_size):
        items = self.reader.read(fetch_size)
        processed_items = [self.processor.process(item) for item in items]
        self.writer.write(processed_items)

class Job:
    def __init__(self, steps, retry_limit=3, skip_limit=10, fetch_size=100, parallel=False):
        self.steps = steps
        self.retry_limit = retry_limit
        self.skip_limit = skip_limit
        self.fetch_size = fetch_size
        self.parallel = parallel

    def execute(self):
        start_time = time.time()
        success = True

        if self.parallel:
            # Execute steps in parallel using threads
            threads = []
            for step in self.steps:
                thread = threading.Thread(target=step.execute, args=(self.fetch_size,))
                threads.append(thread)
                thread.start()

            # Wait for all threads to complete
            for thread in threads:
                thread.join()
        else:
            # Execute steps sequentially
            for step in self.steps:
                retry_count = 0
                skip_count = 0
                while retry_count < self.retry_limit:
                    try:
                        step.execute(self.fetch_size)
                        break  # If successful, exit the retry loop
                    except Exception as e:
                        logging.error(f"Error during step execution: {e}")
                        retry_count += 1
                        if retry_count >= self.retry_limit:
                            logging.error("Retry limit reached. Exiting.")
                            success = False
                            raise e  # Retry limit reached, propagate the error
                        logging.warning(f"Retrying... (Attempt {retry_count}/{self.retry_limit})")

                # You can add more sophisticated error handling and logging here
                # For simplicity, we just print errors to the console

                if skip_count < self.skip_limit:
                    logging.warning(f"Skipped {skip_count} items during execution.")

                # Implement any additional post-execution logic if needed

        end_time = time.time()
        duration = end_time - start_time
        logging.info(f"Job execution completed in {duration:.2f} seconds. {'Success' if success else 'Failed'}")

class JobLauncher:
    def launch(self, job):
        job.execute()