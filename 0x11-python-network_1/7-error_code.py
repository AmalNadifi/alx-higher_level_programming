#!/usr/bin/python3
"""The following module takes in a URL,
sends a request to the URL and displays the body of the response
by using requests
"""
import sys
import requests


if __name__ == "__main__":
    # Sending a GET request to the URL provided in the command-line argument
    response = requests.get(sys.argv[1])

    # Checking the status code of the response
    if response.status_code == requests.codes.ok:
        # Displaying the body of the response
        print(response.text)
    else:
        # Handling and displaying an error code if response status is not OK
        print(f"Error code: {response.status_code}")
