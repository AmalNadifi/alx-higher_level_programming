#!/usr/bin/python3
""" The following script takes in a URL,
sends a request to the URL
and displays the body of the response (decoded in utf-8) """
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    # Extracting the URL from the command-line argument
    url = sys.argv[1]

    # Creating a request object for the specified URL
    request = urllib.request.Request(url)
    try:
        # Sending the request and handling the response
        with urllib.request.urlopen(request) as response:
            # Printing the body of the response decoded in ASCII
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        # Handling and displaying the HTTP error code
        print("Error code: {}".format(e.code))
