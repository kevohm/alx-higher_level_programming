#!/usr/bin/python3
"""checks if response json"""
import requests
import sys
p = ""
if len(sys.argv) == 2:
    p = sys.argv[1]
data = requests.post("http://0.0.0.0:5000/search_user", params={"q": p})
try:
    j_d = data.json()
    if len(J_d.keys()) == 0:
        print("No result")
    else:
        print('[{}] {}'.format(j_d['id'], j_d['name']))
except requests.exceptions.JSONDecodeError as e:
    print("Not a valid JSON")
