#!/usr/bin/python3
""" The following module takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response """
import urllib.request
import sys


if __name__ == "__main__":
    # Creating a request object for the specified URL
    request_obj = urllib.request.Request(sys.argv[1])

    # Sending the request and handling the response
    with urllib.request.urlopen(request_obj) as response:
        # Extracting the headers from the response
        header = dict(resp.headers)
        
        # Printing the value of the 'X-Request-Id' header
        print(header.get("X-Request-Id"))
