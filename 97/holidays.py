from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup as Soup


# prep data
holidays_page = os.path.join('/tmp', 'us_holidays.php')
urlretrieve('https://bit.ly/2LG098I', holidays_page)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup = Soup(content, "html.parser")
    rows = soup.select(".list-table tbody tr")
    for row in rows:
        cells = row.select("td")
        holiday_month = cells[1].select_one("time").get("datetime")[5:7]
        holiday_name = cells[3].getText().strip()
        holidays[holiday_month].append(holiday_name)

    return holidays
