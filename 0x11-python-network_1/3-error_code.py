#!/usr/bin/python3
"""Script takes in a URL, sends a request and displays the response body
(decoded in utf-8)"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req_url = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req_url) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
