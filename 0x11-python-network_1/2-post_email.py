#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""

import sys
from urllib import request, parse

if __name__ == "__main__":
    if len(sys.argv) == 2:
        data = {"email": str(sys.argv[2])}
        data = parse.urlencode(data)
        data = data.encode('ascii')
        with request.urlopen(sys.argv[1], data) as r:
            response = r.open()
            print(response.decode('UTF-8'))
