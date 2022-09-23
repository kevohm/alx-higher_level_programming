#!/usr/bin/python3
"""displays the value of the variable X-Request-Id in the response header"""
import requests
import sys

if len(sys.argv) == 2:
    data = requests.get(sys.argv[1])
    print(data.headers["X-Request-Id"])
