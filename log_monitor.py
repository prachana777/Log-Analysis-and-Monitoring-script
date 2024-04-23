import logging
import signal
import sys
import re

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Set the root logger level to DEBUG

# Define full path to log file
log_file = r"C:\Users\Rachana P\Desktop\Devops\Devops projects\Assignment\example.log"

# Define keywords to monitor
keywords = ["error", "warning", "exception"]

# Define signal handler for graceful exit
def signal_handler(sig, frame):
    print("\nLog monitoring stopped.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Function to monitor log file
def monitor_log():
    try:
        with open(log_file, "r") as file:
            # Loop to continuously monitor log file
            while True:
                # Read the new lines in the log file
                new_lines = file.readlines()
                
                # Print new log entries in real-time
                for line in new_lines:
                    print(line.strip())

                    # Count occurrences of keywords
                    for keyword in keywords:
                        if re.search(keyword, line, re.IGNORECASE):
                            print(f"Keyword '{keyword}' found!")

                # Check for KeyboardInterrupt to stop monitoring
                if KeyboardInterrupt:
                    raise KeyboardInterrupt

    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
        sys.exit(0)

    except FileNotFoundError:
        logging.error(f"Log file '{log_file}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    monitor_log()
