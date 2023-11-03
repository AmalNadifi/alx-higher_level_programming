#!/usr/bin/python3
"""The following script lists the 10 most recent commits
    on a given GitHub repository
    --The script takes2 args (repo name and owner name)
"""
import sys
import requests


if __name__ == "__main__":
    # Constructing the URL for accessing the GitHub repository commits
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    # Sending a GET request to the constructed URL
    response = requests.get(url)

    # Parsing the response as JSON
    commits = response.json()

    try:
        # Iterating through first 10 commits
        # and displaying their SHA and author's name
        for x in range(10):
            print("{}: {}".format(
                commits[x].get("sha"),
                commits[x].get("commit").get("author").get("name")))
    except IndexError:
        # Handling the case when there are fewer than 10 commits
        pass
