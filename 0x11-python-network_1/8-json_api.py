#!/usr/bin/python3
""""""
import requests
import sys
p = ""
if len(sys.argv) == 2:
    p = sys.argv[1]
data = requests.post("http://0.0.0.0:5000/search_user", params={"q": p})
print(data.text)
