#!/usr/bin/python3
"""Script takes in a URL, sends a request to the URL and displays
the response body"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    req_url = requests.get(url)
    if req_url.status_code >= 400:
        print("Error code: {}".format(req_url.status_code))
    else:
        print(req_url.text)
