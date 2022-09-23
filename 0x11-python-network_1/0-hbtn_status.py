#!/usr/bin/python3

from urllib import request

url = 'https://alx-intranet.hbtn.io/status'
with request.urlopen(url) as response:
    page = response.read()
    t_data = type(page)
    decoded = page.decode("UTF-8")
    data = 'Body response: \n\t - type:
        {}\n\t - content: {}\n\t - utf8 content: {}'
    print(data.format(page, t_data, decoded))
