#!/usr/bin/python3
"""Script fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    req_url = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(req_url.text)))
    print("\t- content: {}".format(req_url.text))
