#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.

Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    """Send a POST request with email as a parameter"""
    response = requests.post(url, data={'email': email})

    """Display the body of the response"""
    print(response.text)
