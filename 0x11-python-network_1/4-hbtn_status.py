#!/usr/bin/python3
"""Fetching https://alx-intranet.hbtn.io/status."""
import requests

if __name__ == "__main__":
    # Sending a GET request to the specified URL
    response = requests.get("https://alx-intranet.hbtn.io/status")

    # Printing the body response information
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
