# step.py
class Step:
    def __init__(self, reader, processor, writer):
        self.reader = reader
        self.processor = processor
        self.writer = writer

    def execute(self, fetch_size):
        items = self.reader.read(fetch_size)
        processed_items = [self.processor.process(item) for item in items]
        self.writer.write(processed_items)
