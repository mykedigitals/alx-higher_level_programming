#!/usr/bin/python3
""" This will send a POST request to a given URL with a given email.
Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    result = {"email": sys.argv[2]}

    res = requests.post(url, data=result)
    print(res.text)
