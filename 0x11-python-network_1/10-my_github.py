#!/usr/bin/python3
"""A script that takes in a GitHub username and password (personal access token)
and uses the GitHub API to display the user id
"""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    headers = {"Accept": "application/vnd.github.v3+json"}
    auth = (username, token)

    response = requests.get(url, headers=headers, auth=auth)

    if response.status_code == 200:
        data = response.json()
        print(data["id"])
    else:
        print("None")
