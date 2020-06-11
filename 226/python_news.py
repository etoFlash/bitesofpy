from collections import namedtuple

from bs4 import BeautifulSoup
import requests

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html

Entry = namedtuple('Entry', 'title points comments')


def _create_soup_obj(url):
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    return BeautifulSoup(resp.text, "html.parser")


def get_top_titles(url, top=5):
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    soup = _create_soup_obj(url)
    titles = []

    for title in soup.find_all("span", attrs={"class": "title"}):
        con = title.find_next("span", attrs={"class": "controls"})
        con = con.text.strip().split(" ")
        titles.append(Entry(title=title.text.strip(),
                            points=int(con[0]),
                            comments=int(con[-2])))

    return sorted(titles, reverse=True,
                  key=lambda x: (x.points, x.comments))[:top]
