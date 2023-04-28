#!/usr/bin/python3
"""
A script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import sys
import requests


if __name__ == "__main__":
    # Check if a letter is passed as an argument
    letter = "" if len(sys.argv) == 1 else sys.argv[1]

    # Set the payload data with the letter
    payload = {"q": letter}

    # Send a POST request with the payload to the specified URL
    try:
        r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)

    # Decode the response content
    try:
        response = r.json()
    except ValueError:
        print("Not a valid JSON")
        sys.exit(1)

    # Check if the response is empty or not
    if response:
        print("[{}] {}".format(response.get("id"), response.get("name")))
    else:
        print("No result")

