#!/usr/bin/python3
""" a Python script that takes in a URL, sends a request
to the URL and displays the body of the response."""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    """Send a request to the URL"""
    response = requests.get(url)

    """Check the status code and print the appropriate message"""
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
