#!/usr/bin/python3
"""Script takes in a URL, sends a request and displays a value"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    req_url = urllib.request.Request(url)
    with urllib.request.urlopen(req_url) as response:
        print(dict(response.headers).get("X-Request-Id"))
