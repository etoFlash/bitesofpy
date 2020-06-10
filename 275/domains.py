from collections import Counter

from bs4 import BeautifulSoup as Soup
import requests

COMMON_DOMAINS = ("https://bites-data.s3.us-east-2.amazonaws.com/"
                  "common-domains.html")
TARGET_DIV = {"class": "middle_info_noborder"}


def get_common_domains(url=COMMON_DOMAINS):
    """Scrape the url return the 100 most common domain names"""
    domains = []
    r = requests.get(url)
    r.raise_for_status()
    soup = Soup(r.text, "html.parser")
    for tr in soup.find("div", TARGET_DIV).find_all("tr"):
        domains.append(tr.find_all("td")[2].text)

    return domains


def get_most_common_domains(emails, common_domains=None):
    """Given a list of emails return the most common domain names,
       ignoring the list (or set) of common_domains"""
    if common_domains is None:
        common_domains = get_common_domains()

    filtered = [email.split("@")[-1] for email in emails
                if email.split("@")[-1] not in common_domains]

    return Counter(filtered).most_common()
