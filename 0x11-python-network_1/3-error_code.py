#!/usr/bin/python3
"""displays the body of the response (decoded in utf-8)"""
from urllib.error import HTTPError
from urllib import request
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            with request.urlopen(sys.argv[1]) as r:
                print(r.read().decode("utf-8"))
        except HTTPError as e:
            print("Error code: {}".format(e.code))
