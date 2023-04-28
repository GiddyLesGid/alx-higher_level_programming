#!/usr/bin/python3

"""
A script that takes in a URL and an email address as command line arguments,
sends a POST request to the URL with the email as a parameter,
and displays the body of the response.

Usage:
./posting_email.py <URL> <email>
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # encode the email parameter and prepare the request
    data = urllib.parse.urlencode({"email": email}).encode("ascii")
    request = urllib.request.Request(url, data)

    # send the request and display the response body
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
