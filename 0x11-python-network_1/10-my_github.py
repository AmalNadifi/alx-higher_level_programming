#!/usr/bin/python3
"""Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to
display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    # Creating an HTTPBasicAuth object with the provided username and password
    github_auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    # Sending a GET request to the GitHub API for the user information
    response = requests.get("https://api.github.com/user", auth=github_auth)

    # Parsing the JSON response and extracting the user id
    user_id = response.json().get("id")

    # Displaying the user id
    print(user_id)
