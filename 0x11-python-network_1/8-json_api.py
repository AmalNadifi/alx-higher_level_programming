#!/usr/bin/python3
"""takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import sys
import requests


if __name__ == "__main__":
    # Determine the value of the letter based on command-line arguments
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    # Sending a POST request to the specified URL with the payload
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        # Parsing the response as JSON
        json_resp = response.json()
        if json_resp == {}:
            # Handling the case when there is no result
            print("No result")
        else:
            # Displaying the response with id and name
            print("[{}] {}".format(json_resp.get("id"), json_resp.get("name")))
    except ValueError:
        # Handling the case when the response is not valid JSON
        print("Not a valid JSON")
