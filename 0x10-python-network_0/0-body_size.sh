#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
# Use curl to send a GET request and count the bytes of the response body
curl -s "$1" | wc -c
