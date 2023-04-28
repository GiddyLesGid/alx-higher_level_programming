#!/usr/bin/python3

"""
Displays the X-Request-Id header variable of a request to a given URL.
The X-Request-Id header is a unique identifier that is often used in web applications
to track requests and responses between the client and server. It allows developers
to trace the path of a request through various systems and diagnose issues that may
arise during processing. 

Usage: python3 script.py <url>

Example: python3 script.py https://www.example.com
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
