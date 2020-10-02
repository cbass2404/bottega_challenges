"""
go to dailysmarty.com/topics/python
program to parse through data
select all links that go to post
convert link title text to string

recommendations:

Libraries:
requests
inflection
beatifulsoup


"""

import requests as req
from bs4 import BeautifulSoup as bs


def html_scraper(url, search_content, tag_target, tag_content):
    r = req.get(url)
    soup = bs(r.text, 'html.parser')
    items = soup.find_all(tag_target)

    item_list = []

    for item in items:
        try:
            if search_content in item.get(tag_content):
                item_list.append(item.text)
        except TypeError:
            pass
    return '\n'.join(map(str, item_list))


print(html_scraper('http://dailysmarty.com/topics/python', 'posts/', 'a', 'href'))
