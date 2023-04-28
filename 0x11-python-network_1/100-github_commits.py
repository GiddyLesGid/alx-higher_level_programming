#!/usr/bin/python3
"""
Python script that shows the last 10 commits of a repository
in GitHub
"""
import requests
import sys


def get_commits(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    if response.ok:
        return response.json()
    else:
        response.raise_for_status()


if __name__ == "__main__":
    try:
        owner = sys.argv[1]
        repo = sys.argv[2]
        commits = get_commits(owner, repo)[:10]
        for commit in commits:
            print(f"{commit['sha']}: {commit['commit']['author']['name']}")
    except (IndexError, requests.exceptions.HTTPError):
        pass


