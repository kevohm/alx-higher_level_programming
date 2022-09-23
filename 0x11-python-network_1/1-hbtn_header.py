#!/usr/bin/python3
"""displays the value of the X-Request-Id header variable."""

from urllib import request
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        with request.urlopen(sys.argv[1]) as r:
            print(r.headers['X-Request-Id'])
