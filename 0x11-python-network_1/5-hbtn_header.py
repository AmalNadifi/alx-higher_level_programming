#!/usr/bin/python3
"""The following module takes in a URL, sends a request to the URL,
and displays the value of the variable
X-Request-Id in the response header using requests
"""
import sys
import requests

if __name__ == "__main__":
    # Sending a GET request to the URL provided in the command-line argument
    response = requests.get(sys.argv[1])

    # Displaying value of the 'X-Request-Id' variable in the response header
    print(response.headers.get("X-Request-Id"))
