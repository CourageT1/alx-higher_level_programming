#!/bin/bash
# Bash scripts that sends a POST request to a given URL.

if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"
email="test@gmail.com"
subject="I will always be here for PLD"

# Use curl to send a POST request with the specified variables in the request body
response=$(curl -s -X POST "$url" -d "email=$email&subject=$subject")

# Check if the curl request was successful
if [ $? -eq 0 ]; then
    echo "Response Body:"
    echo "$response"
else
    echo "Error: Failed to send POST request."
fi
