#!/bin/bash
#  Script takes in a URL, sends POST request, and displays the response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
