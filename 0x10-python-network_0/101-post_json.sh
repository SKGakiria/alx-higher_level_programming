#!/bin/bash
# Script sends a JSON POST request to URL as 1st arg., displays response body
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
