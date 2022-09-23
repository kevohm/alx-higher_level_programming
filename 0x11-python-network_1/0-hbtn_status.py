#!/usr/bin/python3
# code to fetch data
from urllib import request

url = 'https://alx-intranet.hbtn.io/status'
with request.urlopen(url) as response:
    print("Body response:")
    page = response.read()
    data = '\t - type: {}\n\t - content: {}\n\t - utf8 content: {}'
    print(data.format(page, type(page), page.decode('UTF-8')))
