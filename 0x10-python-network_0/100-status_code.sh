#!/bin/bash
# Sends a GET request to a given URL and display the response status code.

if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"

# Use curl to send a GET request and display only the status code
curl -s -o /dev/null -w "%{http_code}" "$url"
