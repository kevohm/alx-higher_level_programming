#!/usr/bin/python3

from urllib import request

url = 'https://alx-intranet.hbtn.io/status'
response = request.urlopen(url)
page = response.read()
t_data = type(page)
decoded = page.decode("UTF-8")
print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(page, t_data, decoded))
