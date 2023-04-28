#!/usr/bin/python3
"""
Fetches the 10 most recent commits of a given GitHub repository for a user.
"""

import sys
import requests


def fetch_commits(repo_name: str, owner_name: str) -> None:
    """
    Fetches the 10 most recent commits of a given GitHub repository for a user
    and prints the SHA and the author name.

    Args:
        repo_name (str): Name of the repository.
        owner_name (str): Owner of the repository.

    Returns:
        None
    """
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    # Sends a GET request to the GitHub API
    response = requests.get(url)

    # Parses the JSON response into a Python dictionary
    commits = response.json()

    # Prints the SHA and the author name of the 10 most recent commits
    for i in range(10):
        sha = commits[i].get("sha")
        author = commits[i].get("commit").get("author").get("name")
        print(f"{sha}: {author}")


if __name__ == "__main__":
    # Gets the repository name and owner name from command-line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Fetches the 10 most recent commits for the given repository and owner
    fetch_commits(repo_name, owner_name)

