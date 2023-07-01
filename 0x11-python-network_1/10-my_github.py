#!/usr/bin/python3
"""Script takes your GitHub credentials (username and password) and uses the
GitHub API to display your id"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    a_items = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req_url = requests.get('https://api.github.com/user', auth=a_items)
    print(req_url.json().get("id"))
