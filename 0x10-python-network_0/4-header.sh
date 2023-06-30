#!/bin/bash
# Script takes in URL as arg., sends GET request, displays the response body
curl -s -H "X-School-User-Id: 98" "$1"
