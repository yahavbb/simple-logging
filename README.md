# Python Syslog Logger

A Python script for configuring and running a logging system that sends log messages to both a syslog server and a local syslog daemon, as well as to the standard output (stdout).

## Features

- Configures logging to:
  - Remote Syslog Server
  - Local Syslog Daemon
  - Standard Output (stdout)

- Interactive log message entry with selectable log levels.

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yahavbb/simple-logging.git
   ```

2. Navigate to the project directory:

   ```bash
   cd simple-logging
   ```

3. Make sure you have Python installed on your system.

4. Run the script:

   ```bash
   python syslog_logger.py
   ```

5. Follow the prompts to enter log messages and select log levels.

## Configuration

- You can modify the `LOGGING` dictionary in the `syslog_logger.py` script to customize the logging configuration, including log formats, handlers, and loggers.

- The `LOG_LEVEL_MAPPING` dictionary can be adjusted to map user-input log levels to different logging module log levels.

## Dependencies

- Python 3.x
- Standard Python libraries (no external dependencies)
  
## Acknowledgments

- The script is based on Python's built-in logging module.

---

Feel free to contribute, report issues, or make suggestions to improve this logger. Happy logging!
```
