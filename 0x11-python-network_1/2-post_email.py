#!/usr/bin/python3
"""Script takes in URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response (decoded
in utf-8)"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(val).encode("ascii")

    req_url = urllib.request.Request(url, data)
    with urllib.request.urlopen(req_url) as response:
        print(response.read().decode("utf-8"))
