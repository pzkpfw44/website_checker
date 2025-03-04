# Website Availability Checker

This is a simple Python script to check if websites are online and measure their response times. It helps with website monitoring and diagnosing connectivity issues.

## Features
- Checks if a website is **online** or **offline**.
- Measures **response time** for each request.
- Handles **timeouts** and other connection errors.
- Supports **multiple websites** in one command.

## Installation & Usage

### Step 1: Install Dependencies
```bash

pip install requests

If you enter a URL without http:// or https://, the script automatically adds https:// to ensure proper connectivity.

Future Improvements
Save results to a log file.
Check websites at regular intervals.
Send email or Slack notifications for downtime alerts.
Requirements
Python 3.x
requests library (pip install requests)
License
This project is licensed under the MIT License. 
