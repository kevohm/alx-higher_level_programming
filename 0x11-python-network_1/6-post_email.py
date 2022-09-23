#!/usr/bin/python3
"""sends a POST request to the passed URL with the email """
import sys
import requests

if __name__ == "__main__":
    data = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(data.text)
