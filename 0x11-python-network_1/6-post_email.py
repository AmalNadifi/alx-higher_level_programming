#!/usr/bin/python3
"""The following module takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    # Extracting the URL and email from command-line arguments
    url = sys.argv[1]
    email_value = {"email": sys.argv[2]}

    # Sending a POST request with the URL and email data
    response = requests.post(url, data=email_value)

    # Displaying the body of the response
    print(response.text)
