#!/usr/bin/python3
"""fetch from github"""
from sys import argv
import requests
if len(argv) == 3:
    url = 'https://api.github.com/repos/{}/{}/commits?per_page=10'
    data = requests.get(url.format(argv[2], argv[1]))
    r_dict = data.json()
    for i in r_dict:
        sha = i.get('sha')
        author = i.get('commit').get('author').get('name')
        print(f'{sha}: {author}')
