#!/usr/bin/python3
"""
Lists the 10 most recent commits on a given GitHub repository.
"""

import sys
import requests


def get_recent_commits(owner, repo):
    """
    Retrieves the 10 most recent commits of a GitHub repository.

    Args:
        owner (str): The repository owner's GitHub username.
        repo (str): The name of the repository.

    Returns:
        List of dictionaries representing the 10 most recent commits. Each
        dictionary contains the commit's SHA hash and author name.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    r = requests.get(url)
    if r.status_code != 200:
        print(f"Error: Could not retrieve commits from {url}")
        sys.exit(1)
    commits = r.json()
    recent_commits = []
    for i in range(min(10, len(commits))):
        commit_info = {"sha": commits[i].get("sha"),
                       "author": commits[i].get("commit").get("author").get("name")}
        recent_commits.append(commit_info)
    return recent_commits


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./recent_commits.py <owner> <repo>")
        sys.exit(1)

    owner = sys.argv[1]
    repo = sys.argv[2]
    recent_commits = get_recent_commits(owner, repo)

    for commit in recent_commits:
        print("{}: {}".format(commit["sha"], commit["author"]))


