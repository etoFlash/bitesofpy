from collections import Counter

from bs4 import BeautifulSoup as Soup
import requests

AMAZON = "amazon.com"
# static copy
TIM_BLOG = ('https://bites-data.s3.us-east-2.amazonaws.com/'
            'tribe-mentors-books.html')
MIN_COUNT = 3


def load_page():
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(TIM_BLOG).content.decode('utf-8')


def get_top_books(content=None):
    """Make a BeautifulSoup object loading in content,
       find all links that contain AMAZON, extract the book title
       and count them.
       Return a list of (title, count) tuples where
       count is at least MIN_COUNT
    """
    if content is None:
        content = load_page()
    # code here ...
    links_counter = Counter()
    s = Soup(content, "html.parser")
    for link in s.select("a"):
        if AMAZON in link.get("href").lower():
            links_counter[link.text] += 1

    top_books = []
    for rec in links_counter.most_common():
        if rec[1] < MIN_COUNT:
            break
        top_books.append(rec)

    return top_books
