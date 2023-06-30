#!/bin/bash
# Script sends request to URL as 1st arg., displays only response status code
curl -s -o /dev/null -w "%{http_code}" "$1"
