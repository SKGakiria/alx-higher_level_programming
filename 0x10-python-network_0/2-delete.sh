#!/bin/bash
# Script sends DELETE request to URL passed as 1st arg., displays response body
curl -s -X DELETE "$1"
