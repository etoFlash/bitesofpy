import csv
from collections import OrderedDict

import requests

CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    return requests.get(CSV_URL).text.splitlines(keepends=False)


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and print a table of timezones
       and their corresponding member counts in pluses to standard output
    """
    timezones = OrderedDict()
    for row in csv.DictReader(content):
        timezones[row["tz"]] = timezones.get(row["tz"], 0) + 1

    for tz, counter in timezones.items():
        print("{0:21}| {1}".format(tz, "+" * counter))
