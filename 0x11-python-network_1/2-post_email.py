#!/usr/bin/python3
""" a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]  """Get the URL from command line arguments"""
    email = sys.argv[2]  """Get the email from command line arguments"""

    """Encode the email parameter for the POST request"""
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data=data) as response:
        """Read and decode the response body in utf-8"""
        content = response.read().decode('utf-8')

    print(content)
