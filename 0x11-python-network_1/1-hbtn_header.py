#!/usr/bin/python3
""" The following module takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response """
import urllib.request
import sys


# Checking if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    sys.stderr.write("Usage: {} <URL>\n".format(sys.argv[0]))
    sys.exit(1)

# Extracting the URL from the command-line argument
url = sys.argv[1]

try:
    # Making a request to the specified URL and handling the response
    with urllib.request.urlopen(url) as response:
        # Checking if the 'X-Request-Id' header is present in the response
        if 'X-Request-Id' in response.headers:
            x_request_id = response.headers['X-Request-Id']
            print(x_request_id)
        else:
            # Indicating that 'X-Request-Id' was not found in response headers
            sys.stderr.write("X-Request-Id not found in response headers\n")
            sys.exit(1)
except urllib.error.URLError as e:
    # Handling and displaying errors in case of issues with the request
    sys.stderr.write("Error while making the request: {}\n".format(e))
    sys.exit(1)
