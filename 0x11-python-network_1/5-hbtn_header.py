#!/usr/bin/python3
"""Script takes in a URL, sends a request and displays the value of the
variable X-Request-Id in the response header"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    req_url = requests.get(url)
    print(req_url.headers.get("X-Request-Id"))
