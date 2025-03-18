# Q3. Uptime Monitoring and Alert System:
# Write a Python script that checks the uptime of provided URLs and notifies the user if any of the URLs return 4xx or 5xx HTTP status codes. For demonstration purposes, use the following URLs:
# 4xx (Client Error):
# http://www.example.com/nonexistentpage
# http://httpstat.us/404
# 5xx (Server Error):
# http://httpstat.us/500
# 200 (Successful Response):
# https://www.google.com/

# Requirements:
# URL Check: The script should check the provided URLs and get their HTTP status codes. - Done
# Handle Multiple URLs: The script should be able to handle multiple URLs at once, checking each one. - Done
# Error Detection: If the status code of any URL is either 4xx or 5xx, the program should: Notify the user via a print message. - Done
# Loop and Monitor: You should set up a simple loop that continuously monitors the URLs for a certain interval (e.g., every 10 seconds) to simulate a basic uptime monitoring system. - Done
# Status Message: For each URL, the script should output the URL and its current HTTP status code (e.g., 200 OK, 404 Not Found). - Done

# Bonus (Optional):
# Implement an exponential backoff in case of multiple consecutive errors (e.g., retry after increasing intervals).
# Add logging functionality to save the status check results to a log file.


import requests
import re
from requests.exceptions import RequestException

import time 
import schedule

def uptime_check(url):
    for i in url:

        try:
            response = requests.get(i)
            status_code = response.status_code
            status_message = response.reason

            print(f"Checking URL: {i}")

            if re.search("^2\d{2}$", str(status_code)):
                print(f"Status Code: {status_code} : {status_message}\nThe website is UP and running.")
            elif re.search("^4\d{2}$", str(status_code)):
                print(f"Status Code: {status_code} : {status_message}\nALERT: 4xx error encountered for URL: {i}")
            elif re.search("^5\d{2}$", str(status_code)):
                print(f"Status Code: {status_code} : {status_message}\nALERT: 5xx error encountered for URL: {i}")
        
        except RequestException as e:
            print(f"Error: {e}")
        
        print("")

url = list((input("Enter valid URL(s): ")).split())
interval = int(input("Enter the interval for monitoring: "))

schedule.every(interval).seconds.do((lambda: uptime_check(url)))

try:
    uptime_check(url)
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")


# Example Expected Output (if status codes are returned):
# Checking URL: http://www.example.com/nonexistentpage
# Status Code: 404 Not Found
# ALERT: 4xx error encountered for URL: http://www.example.com/nonexistentpage

# Checking URL: http://httpstat.us/500
# Status Code: 500 Internal Server Error
# ALERT: 5xx error encountered for URL: http://httpstat.us/500

# Checking URL: https://www.google.com/
# Status Code: 200 OK
# The website is UP and running.