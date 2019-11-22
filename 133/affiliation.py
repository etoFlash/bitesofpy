import re


def generate_affiliation_link(url):
    amazon_url_pattern = r"https?://(www.)?amazon(.[a-z]{2,3}){1,2}/[a-zA-Z0-9-]*?/dp/([0-9A-Z]*)"
    book_id = re.search(amazon_url_pattern, url).group(3)
    return f"http://www.amazon.com/dp/{book_id}/?tag=pyb0f-20"
