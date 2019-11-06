from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

CONTENT = requests.get('http://bit.ly/2EN2Ntv').text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, 'html.parser')
    book = Book(soup.select(".dotd-title h2")[0].getText().strip(),
                soup.select(".dotd-main-book-summary div")[2].getText().strip(),
                soup.select("img.imagecache-dotd_main_image")[0]["src"],
                soup.select(".dotd-main-book-image a")[0]["href"])
    return book
