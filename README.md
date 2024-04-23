# Log-Analysis-and-Monitoring-script

This script continuously monitors a specified log file for new entries, tracks and displays new log entries in real-time, implements a mechanism to stop the monitoring loop using a signal like Ctrl+C, and performs basic analysis on log entries by counting occurrences of specific keywords and generating summary reports.

Prerequisites:
Python 3.x installed on your system.

Installation:
Clone this repository to your local machine: git clone “github link”
Navigate to the directory containing the script: cd log-monitoring-script

Usage:
Ensure that the log file you want to monitor (example.log) is located in the same directory as the script.
Open a terminal or command prompt and navigate to the directory containing the script.
Run the script using the following command: python log_monitor.py
The script will start monitoring the log file and display new log entries in real-time. Press Ctrl+C to stop monitoring.

Log Analysis:
The script performs basic analysis on log entries by counting occurrences of specific keywords (e.g., "error", "warning", "exception") and generating a summary report.

File Structure:
log_monitor.py: The main Python script for monitoring the log file.
example.log: Example log file containing sample log entries for testing.

Contributing:
Contributions are welcome! Please feel free to submit issues or pull requests if you have any suggestions or improvements for the script.
