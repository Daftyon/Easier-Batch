# Easier Batch - Python Batch Processing Framework
<img width="602" height="160" alt="image" src="https://github.com/user-attachments/assets/a3e808a6-b271-4e69-b82d-00a740a39c8f" />


A comprehensive, Spring Batch-inspired batch processing framework for Python that provides robust, scalable, and fault-tolerant batch job execution capabilities.

## 🚀 Overview

This framework implements enterprise-grade batch processing patterns in Python, offering a clean separation of concerns through the **Reader-Processor-Writer** pattern. It's designed for processing large volumes of data efficiently with built-in error handling, retry mechanisms, transaction management, and comprehensive job monitoring.

## 🏗️ Architecture
### Core Components Flow

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   ItemReader    │───▶│  ItemProcessor   │───▶│   ItemWriter   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                        │                        │
         └────────────────────────┼────────────────────────┘
                                  │
                            ┌─────▼─────┐
                            │    Step   │
                            └─────┬─────┘
                                  │
                            ┌─────▼─────┐
                            │    Job    │
                            └─────┬─────┘
                                  │
                            ┌─────▼─────┐
                            │JobLauncher│
                            └───────────┘
```

### Complete Framework Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           EASIER BATCH FRAMEWORK                                │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  ┌─────────────────┐    ┌──────────────────┐    ┌─────────────────────────────┐ │
│  │  PRESENTATION   │    │    BUSINESS      │    │      INFRASTRUCTURE         │ │
│  │     LAYER       │    │     LAYER        │    │        LAYER                │ │
│  └─────────────────┘    └──────────────────┘    └─────────────────────────────┘ │
│           │                       │                           │                 │
│           ▼                       ▼                           ▼                 │
│  ┌─────────────────┐    ┌──────────────────┐    ┌─────────────────────────────┐ │
│  │                 │    │                  │    │                             │ │
│  │ • CLI Interface │    │ • Job Management │    │ • Database Connections      │ │
│  │ • Web Dashboard │    │ • Step Execution │    │ • Transaction Management    │ │
│  │ • REST API      │    │ • Error Handling │    │ • Retry Mechanisms          │ │
│  │ • Monitoring    │    │ • Progress Track │    │ • Metadata Storage          │ │
│  │                 │    │                  │    │                             │ │
│  └─────────────────┘    └──────────────────┘    └─────────────────────────────┘ │
│                                                                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│                              CORE ENGINE                                        │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  ┌──────────────────────────────────────────────────────────────────────────┐   │
│  │                        JOB EXECUTION ENGINE                              │   │
│  │                                                                          │   │
│  │  ┌─────────────────┐  ┌──────────────────┐  ┌─────────────────────────┐  │   │
│  │  │   JobLauncher   │  │       Job        │  │     Scheduler           │  │   │
│  │  │                 │  │                  │  │                         │  │   │
│  │  │ • Configuration │  │ • Steps[]        │  │ • Cron Jobs             │  │   │
│  │  │ • Validation    │  │ • Parameters     │  │ • Triggers              │  │   │
│  │  │ • Launch Logic  │  │ • Parallel Exec  │  │ • Event-based           │  │   │
│  │  │ • Monitoring    │  │ • Restart Logic  │  │ • Queue Management      │  │   │
│  │  │                 │  │                  │  │                         │  │   │
│  │  └─────────────────┘  └──────────────────┘  └─────────────────────────┘  │   │
│  └──────────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
│  ┌──────────────────────────────────────────────────────────────────────────┐   │
│  │                        STEP EXECUTION ENGINE                             │   │
│  │                                                                          │   │
│  │  ┌─────────────────┐  ┌──────────────────┐  ┌─────────────────────────┐  │   │
│  │  │      Step       │  │   Chunk Manager  │  │   Parallel Processor    │  │   │
│  │  │                 │  │                  │  │                         │  │   │
│  │  │ • Read-Process- │  │ • Commit Points  │  │ • Multi-threading       │  │   │
│  │  │   Write Cycle   │  │ • Rollback       │  │ • Resource Sharing      │  │   │
│  │  │ • Error Handling│  │ • Batch Size     │  │ • Load Balancing        │  │   │
│  │  │ • Progress Track│  │ • Memory Mgmt    │  │ • Synchronization       │  │   │
│  │  │                 │  │                  │  │                         │  │   │
│  │  └─────────────────┘  └──────────────────┘  └─────────────────────────┘  │   │
│  └──────────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│                           COMPONENT LAYER                                       │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│  ┌─────────────────┐    ┌──────────────────┐    ┌─────────────────────────────┐ │
│  │   READERS       │    │   PROCESSORS     │    │       WRITERS               │ │
│  │                 │    │                  │    │                             │ │
│  │ • FileReader    │    │ • Transformer    │    │ • FileWriter                │ │
│  │ • DatabaseReader│    │ • Validator      │    │ • DatabaseWriter            │ │
│  │ • APIReader     │    │ • Enricher       │    │ • APIWriter                 │ │
│  │ • KafkaReader   │    │ • Filter         │    │ • KafkaWriter               │ │
│  │ • CSVReader     │    │ • Aggregator     │    │ • CSVWriter                 │ │
│  │ • JSONReader    │    │ • Custom Logic   │    │ • JSONWriter                │ │
│  │                 │    │                  │    │                             │ │
│  └─────────────────┘    └──────────────────┘    └─────────────────────────────┘ │
│                                                                                 │
├──────────────────────────────────────────────────────────────────────────────────┤
│                        CROSS-CUTTING CONCERNS                                    │
├──────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  ┌─────────────────┐  ┌──────────────────┐  ┌─────────────────┐  ┌─────────────┐ │
│  │   MONITORING    │  │   RETRY & SKIP   │  │   TRANSACTION   │  │  SECURITY   │ │
│  │                 │  │                  │  │                 │  │             │ │
│  │ • Metrics       │  │ • Retry Policies │  │ • ACID Props    │  │ • Auth      │ │
│  │ • Logging       │  │ • Skip Limits    │  │ • Rollback      │  │ • Authz     │ │
│  │ • Alerting      │  │ • Error Recovery │  │ • Commit        │  │ • Encryption│ │
│  │ • Health Checks │  │ • Circuit Break  │  │ • Isolation     │  │ • Audit     │ │
│  │ • Dashboards    │  │ • Backoff        │  │ • Connection    │  │ • Compliance│ │
│  │                 │  │                  │  │   Pooling       │  │             │ │
│  └─────────────────┘  └──────────────────┘  └─────────────────┘  └─────────────┘ │
│                                                                                  │
├──────────────────────────────────────────────────────────────────────────────────┤
│                           DATA LAYER                                             │
├──────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  ┌─────────────────┐  ┌──────────────────┐  ┌─────────────────┐  ┌─────────────┐ │
│  │   METADATA      │  │   PERSISTENCE    │  │    CACHING      │  │  STORAGE    │ │
│  │   REPOSITORY    │  │                  │  │                 │  │  ADAPTERS   │ │
│  │                 │  │ • Job Metadata   │  │ • Redis         │  │             │ │
│  │ • Job History   │  │ • Step Metadata  │  │ • In-Memory     │  │ • File Sys  │ │
│  │ • Execution     │  │ • Execution      │  │ • Distributed   │  │ • Databases │ │
│  │   Context       │  │   Context        │  │ • Cache Aside   │  │ • Cloud S3  │ │
│  │ • Performance   │  │ • Checkpoints    │  │ • Write-through │  │ • HDFS      │ │
│  │   Metrics       │  │ • Restart Points │  │ • Write-behind  │  │ • REST APIs │ │
│  │                 │  │                  │  │                 │  │             │ │
│  └─────────────────┘  └──────────────────┘  └─────────────────┘  └─────────────┘ │
│                                                                                  │
└──────────────────────────────────────────────────────────────────────────────── ─┘
```

### Detailed Component Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                        ITEMREADER ARCHITECTURE                                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│                        ┌─────────────────┐                                      │
│                        │   ItemReader    │                                      │
│                        │   (Abstract)    │                                      │
│                        │                 │                                      │
│                        │ + read(size)    │                                      │
│                        │ + progress()    │                                      │
│                        │ + close()       │                                      │
│                        └─────────────────┘                                      │
│                                 │                                               │
│                                 ▼                                               │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────┐ │
│  │   FileReader    │  │ DatabaseReader  │  │   APIReader     │  │ KafkaReader │ │
│  │                 │  │                 │  │                 │  │             │ │
│  │ • CSV Support   │  │ • SQL Queries   │  │ • REST/GraphQL  │  │ • Topics    │ │
│  │ • JSON Support  │  │ • Pagination    │  │ • Auth Handling │  │ • Partitions│ │
│  │ • XML Support   │  │ • Connection    │  │ • Rate Limiting │  │ • Consumers │ │
│  │ • Binary Files  │  │   Pooling       │  │ • Retry Logic   │  │ • Offsets   │ │
│  │ • Compression   │  │ • Transactions  │  │ • Circuit Break │  │ • Groups    │ │
│  │ • Encoding      │  │ • Cursors       │  │                 │  │             │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘  └─────────────┘ │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                       ITEMPROCESSOR ARCHITECTURE                                │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│                        ┌─────────────────┐                                      │
│                        │ ItemProcessor   │                                      │
│                        │   (Abstract)    │                                      │
│                        │                 │                                      │
│                        │ + process(item) │                                      │
│                        │ + validate(item)│                                      │
│                        │ + filter(item)  │                                      │
│                        └─────────────────┘                                      │
│                                 │                                               │
│                                 ▼                                               │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────┐ │
│  │ Transformer     │  │   Validator     │  │    Enricher     │  │ Aggregator  │ │
│  │                 │  │                 │  │                 │  │             │ │
│  │ • Data Mapping  │  │ • Schema Valid  │  │ • Lookup Data   │  │ • Grouping  │ │
│  │ • Type Convert  │  │ • Business Rules│  │ • External APIs │  │ • Counting  │ │
│  │ • Format Change │  │ • Constraints   │  │ • Calculations  │  │ • Summing   │ │
│  │ • Normalization │  │ • Custom Logic  │  │ • Derived Fields│  │ • Averaging │ │
│  │ • Cleansing     │  │ • Error Report  │  │ • ML Inference  │  │ • Min/Max   │ │
│  │                 │  │                 │  │                 │  │             │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘  └─────────────┘ │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                        ITEMWRITER ARCHITECTURE                                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│                        ┌─────────────────┐                                      │
│                        │   ItemWriter    │                                      │
│                        │   (Abstract)    │                                      │
│                        │                 │                                      │
│                        │ + write(items)  │                                      │
│                        │ + flush()       │                                      │
│                        │ + close()       │                                      │
│                        └─────────────────┘                                      │
│                                 │                                               │
│                                 ▼                                               │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────┐ │
│  │   FileWriter    │  │ DatabaseWriter  │  │   APIWriter     │  │ KafkaWriter │ │
│  │                 │  │                 │  │                 │  │             │ │
│  │ • Format Output │  │ • Bulk Inserts  │  │ • REST/GraphQL  │  │ • Topics    │ │
│  │ • Compression   │  │ • Upsert Logic  │  │ • Auth Handling │  │ • Partitions│ │
│  │ • Backup/Archive│  │ • Batch Updates │  │ • Rate Limiting │  │ • Producers │ │
│  │ • Error Handling│  │ • Connection    │  │ • Retry Logic   │  │ • Keys      │ │
│  │ • Rollback      │  │   Pooling       │  │ • Circuit Break │  │ • Headers   │ │
│  │                 │  │ • Transactions  │  │                 │  │             │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘  └─────────────┘ │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### Framework Hierarchy

- **JobLauncher**: Entry point for job execution with configuration management
- **Job**: Container for one or more steps with parallel/sequential execution support
- **Step**: Orchestrates the read-process-write cycle with error handling
- **ItemReader**: Abstract base for reading data from various sources
- **ItemProcessor**: Abstract base for transforming/processing items
- **ItemWriter**: Abstract base for writing processed data to destinations

## 🎯 Key Features

### ✅ **Robust Error Handling**
- **Retry Logic**: Configurable retry policies with exponential backoff
- **Skip Mechanism**: Skip problematic items without failing the entire job
- **Fault Tolerance**: Graceful degradation and recovery from failures

### ✅ **Transaction Management**
- Database transaction support with rollback capabilities
- Chunk-based processing with configurable commit intervals
- Connection pooling and automatic resource management

### ✅ **Comprehensive Monitoring**
- MySQL-based metadata repository for job/step tracking
- Real-time progress monitoring and metrics collection
- Detailed execution history and audit trails

### ✅ **Scalability & Performance**
- Chunk-based processing for memory efficiency
- Parallel step execution support
- Configurable fetch sizes and batch parameters

### ✅ **Enterprise Features**
- Job restart capability from last successful checkpoint
- Configurable execution policies and limits
- Comprehensive logging and debugging support

## 📦 Installation

### Prerequisites
- Python 3.7+
- MySQL 5.7+ or MySQL 8.0+
- Required Python packages:

```bash
pip install mysql-connector-python
```

### Setup
1. Clone the repository
2. Install dependencies
3. Configure database connection
4. Initialize metadata tables

```python
from easier_batch import BatchConfiguration, MetadataManager

config = BatchConfiguration(
    db_host="localhost",
    db_user="your_user",
    db_password="your_password",
    db_database="your_database"
)

metadata_manager = MetadataManager(config)
metadata_manager.create_metadata_tables()
```

## 🚀 Quick Start

### Basic Example

```python
from easier_batch import (
    BatchConfiguration, JobLauncher, Job, Step,
    FileItemReader, StringTransformProcessor, FileItemWriter
)

# 1. Configure the framework
config = BatchConfiguration(
    fetch_size=100,
    retry_limit=3,
    skip_limit=10,
    chunk_size=50
)

# 2. Create components
reader = FileItemReader("input_data.txt")
processor = StringTransformProcessor()
writer = FileItemWriter("output_data.txt")

# 3. Define step
step = Step(
    name="data_transformation_step",
    reader=reader,
    processor=processor,
    writer=writer,
    config=config
)

# 4. Create job
job = Job(
    name="file_processing_job",
    steps=[step],
    config=config,
    job_parameters={"source": "input_data.txt", "target": "output_data.txt"}
)

# 5. Launch job
launcher = JobLauncher(config)
job_id = launcher.launch(job)
print(f"Job launched with ID: {job_id}")
```

### Advanced Example with Custom Components

```python
class DatabaseItemReader(ItemReader):
    def __init__(self, connection_string, query):
        super().__init__()
        self.connection_string = connection_string
        self.query = query
        self.offset = 0
    
    def read(self, fetch_size: int) -> List[Any]:
        # Implementation for database reading
        # with pagination support
        pass

class ValidationProcessor(ItemProcessor):
    def validate_item(self, item: Any) -> bool:
        # Custom validation logic
        return item is not None and len(str(item)) > 0
    
    def process(self, item: Any) -> Any:
        # Custom processing logic
        if not self.validate_item(item):
            raise SkippableException("Invalid item")
        
        # Transform item
        return self.transform(item)

class APIItemWriter(ItemWriter):
    def __init__(self, api_endpoint, auth_token):
        super().__init__()
        self.api_endpoint = api_endpoint
        self.auth_token = auth_token
    
    def write(self, items: List[Any]) -> None:
        # Implementation for API writing
        # with batch posting support
        pass
```

## ⚙️ Configuration

### BatchConfiguration Parameters

```python
config = BatchConfiguration(
    # Processing parameters
    fetch_size=100,           # Items per read operation
    chunk_size=100,          # Items per transaction
    retry_limit=3,           # Max retry attempts
    skip_limit=10,           # Max skippable items
    parallel=False,          # Parallel step execution
    
    # Database configuration
    db_host="localhost",
    db_user="batch_user",
    db_password="password",
    db_database="batch_db",
    
    # Retry policy
    retry_backoff_multiplier=1.5,  # Exponential backoff multiplier
    retry_max_delay=300,          # Max delay between retries (seconds)
    
    # Transaction settings
    transaction_timeout=300       # Transaction timeout (seconds)
)
```

### Retry Policy Configuration

```python
from easier_batch import RetryPolicy

retry_policy = RetryPolicy(
    max_attempts=5,
    base_delay=1.0,          # Initial delay in seconds
    max_delay=60.0,          # Maximum delay in seconds
    backoff_multiplier=2.0   # Exponential backoff multiplier
)
```

## 📊 Database Schema

The framework automatically creates the following metadata tables:

### job_metadata
- `job_id` (Primary Key)
- `job_name`
- `job_parameters` (JSON)
- `status`
- `start_time`
- `end_time`
- `created_by`
- `version`

### step_metadata
- `step_id` (Primary Key)
- `job_id` (Foreign Key)
- `step_name`
- `status`
- `start_time`
- `end_time`
- `read_count`
- `write_count`
- `skip_count`
- `retry_count`
- `error_message`

### execution_context
- `context_id` (Primary Key)
- `job_id` (Foreign Key)
- `step_id` (Foreign Key)
- `context_data` (JSON)
- `context_type`
- `created_at`

## 🔧 Error Handling

### Exception Hierarchy

```python
BatchException                 # Base exception
├── RetryableException        # Exceptions that can be retried
└── SkippableException       # Exceptions that can be skipped
```

### Error Handling Strategies

1. **Retry Strategy**: Automatically retry failed operations with exponential backoff
2. **Skip Strategy**: Skip problematic items and continue processing
3. **Fail Fast**: Immediately fail the job for critical errors
4. **Circuit Breaker**: Prevent cascading failures

### Example Error Handling

```python
class RobustProcessor(ItemProcessor):
    def process(self, item: Any) -> Any:
        try:
            # Processing logic
            return self.complex_transformation(item)
        except ValidationError as e:
            # Skip invalid items
            raise SkippableException(f"Validation failed: {e}")
        except TemporaryServiceError as e:
            # Retry for temporary issues
            raise RetryableException(f"Service temporarily unavailable: {e}")
        except CriticalError as e:
            # Fail fast for critical issues
            raise BatchException(f"Critical error occurred: {e}")
```

## 📈 Monitoring & Metrics

### Real-time Monitoring

```python
# Get job execution status
job_status = metadata_manager.get_job_status(job_id)

# Get step execution metrics
step_metrics = metadata_manager.get_step_metrics(step_id)
print(f"Read: {step_metrics['read_count']}")
print(f"Written: {step_metrics['write_count']}")
print(f"Skipped: {step_metrics['skip_count']}")
print(f"Retries: {step_metrics['retry_count']}")
```

### Progress Tracking

```python
# Reader progress
progress = reader.get_progress()
print(f"Progress: {progress['current_position']}/{progress['total_items']}")

# Writer metrics
written_count = writer.get_written_count()
print(f"Items written: {written_count}")
```

## 🔄 Job Restart & Recovery

The framework supports automatic job restart from the last successful checkpoint:

```python
# Enable restart capability
job = Job(
    name="restartable_job",
    steps=[step],
    config=config,
    job_parameters={"restart_from_failure": True}
)

# Framework automatically handles restart logic
job_id = launcher.launch(job)
```

## 🛠️ Best Practices

### 1. **Chunk Size Optimization**
- Start with chunk sizes of 100-1000 items
- Monitor memory usage and adjust accordingly
- Consider data complexity and processing time

### 2. **Error Handling Strategy**
- Use `RetryableException` for temporary failures
- Use `SkippableException` for data quality issues
- Set appropriate retry and skip limits

### 3. **Resource Management**
- Always use context managers for database connections
- Implement proper cleanup in custom readers/writers
- Monitor connection pool usage

### 4. **Performance Tuning**
- Profile your processors to identify bottlenecks
- Use parallel execution for independent steps
- Optimize database queries and indexes

### 5. **Monitoring & Alerting**
- Set up monitoring for job failures
- Track processing metrics and trends
- Implement alerting for critical thresholds

## 📚 Advanced Features

### Parallel Processing

```python
# Enable parallel step execution
config = BatchConfiguration(parallel=True)

job = Job(
    name="parallel_job",
    steps=[step1, step2, step3],  # Steps run in parallel
    config=config
)
```

### Custom Retry Policies

```python
class CustomRetryPolicy(RetryPolicy):
    def should_retry(self, attempt: int, exception: Exception) -> bool:
        # Custom retry logic based on exception type
        if isinstance(exception, DatabaseConnectionError):
            return attempt < 5
        elif isinstance(exception, ValidationError):
            return False  # Don't retry validation errors
        return super().should_retry(attempt, exception)
```

### Transaction Management

```python
with DatabaseConnection(config) as conn:
    cursor = conn.cursor()
    try:
        # Perform database operations
        cursor.execute("INSERT INTO ...")
        cursor.execute("UPDATE ...")
        # Automatic commit on success
    except Exception:
        # Automatic rollback on failure
        raise
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: Check the inline documentation and examples
- **Issues**: Open an issue on GitHub for bug reports or feature requests
- **Discussions**: Join the discussions for questions and community support

## 🔮 Roadmap

- [ ] Support for additional data sources (Kafka, Redis, S3)
- [ ] Web-based monitoring dashboard
- [ ] Integration with popular orchestration tools (Airflow, Prefect)
- [ ] Enhanced partitioning and scaling capabilities
- [ ] Cloud-native deployment options

---

## 👨‍💻 Author

**Built with ❤️ by Ahmed Hafdi**

*Passionate about creating robust, scalable solutions for enterprise data processing*

---

**Built with ❤️ for robust batch processing in Python - Making batch processing easier than ever!**
