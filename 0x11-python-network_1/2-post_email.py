#!/usr/bin/python3
""" The following module takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    # Creating a dictionary of values with the email parameter
    values_dict = {"email": sys.argv[2]}

    # Encoding the data as ASCII
    data = urllib.parse.urlencode(values_dict)
    data = data.encode('ascii')

    # Creating a POST request with the URL and data
    request = urllib.request.Request(sys.argv[1], data)

    # Sending the request and handling the response
    with urllib.request.urlopen(request) as resp:
        print(resp.read().decode("utf-8"))
