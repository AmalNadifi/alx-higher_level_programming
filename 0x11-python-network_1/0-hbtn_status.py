#!/usr/bin/python3
""" This module  fetches https://alx-intranet.hbtn.io/status """
import urllib.request

# Defining the URL to fetch
url = 'https://alx-intranet.hbtn.io/status'

# Using the 'with' statement to open the URL & ensure proper resource cleanup
with urllib.request.urlopen(url) as response:
    # Reading the content of the response into the 'body' variable
    body = response.read()

    # Getting the 'Content-Type' & charset information from response headers
    content_type = response.info().get('Content-Type')
    charset = response.info().get_param('charset')

    # Displaying the response information as specified
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)

    # If there is a charset specified, decoding the content and displaying it
    if charset:
        print("\t- utf8 content:", body.decode(charset))
    else:
        # Indicating utf8 content is not available if charset is not specified
        print("\t- utf8 content: N/A")
