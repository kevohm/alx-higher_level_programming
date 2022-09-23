#!/usr/bin/python3
""" displays the body of the response"""
import sys
import requests

if __name__ == "__main__":
    data = requests.get(sys.argv[1])
    try:
        if data.status_code > 400:
            data.raise_for_status()
        print(data.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(data.status_code))
