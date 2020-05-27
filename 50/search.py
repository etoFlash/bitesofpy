from collections import namedtuple
from datetime import date
import time
import re

import feedparser

FEED = 'https://bites-data.s3.us-east-2.amazonaws.com/all.rss.xml'

Entry = namedtuple('Entry', 'date title link tags')


def _convert_struct_time_to_dt(stime: time.struct_time):
    """Convert a time.struct_time as returned by feedparser into a
    datetime.date object, so:
    time.struct_time(tm_year=2016, tm_mon=12, tm_mday=28, ...)
    -> date(2016, 12, 28)
    """
    return date(*stime[:3])


def get_feed_entries(feed: feedparser.FeedParserDict = FEED):
    """Use feedparser to parse PyBites RSS feed.
       Return a list of Entry namedtuples (date = date, drop time part)
    """
    f = feedparser.parse(feed)
    return [Entry(date=_convert_struct_time_to_dt(e.published_parsed),
                  title=e.title,
                  link=e.link,
                  tags=[t['term'].lower() for t in e.tags])
            for e in f.entries]


def filter_entries_by_tag(search, entry):
    """Check if search matches any tags as stored in the Entry namedtuple
       (case insensitive, only whole, not partial string matches).
       Returns bool: True if match, False if not.
       Supported searches:
       1. If & in search do AND match,
          e.g. flask&api should match entries with both tags
       2. Elif | in search do an OR match,
          e.g. flask|django should match entries with either tag
       3. Else: match if search is in tags
    """
    tags = re.split(r"[&|]", search)
    result = [tag.lower() in entry.tags
              for tag in tags]

    if search.count("&") and not all(result):
        return False
    elif search.count("|") and not any(result):
        return False
    elif not result[0]:
        return False

    return True


def main():
    """Entry point to the program
       1. Call get_feed_entries and store them in entries
       2. Initiate an infinite loop
       3. Ask user for a search term:
          - if enter was hit (empty string), print 'Please provide a search term'
          - if 'q' was entered, print 'Bye' and exit/break the infinite loop
       4. Filter/match the entries (see filter_entries_by_tag docstring)
       5. Print the title of each match ordered by date ascending
       6. Secondly, print the number of matches: 'n entries matched'
          (use entry if only 1 match)
    """
    entries = get_feed_entries()
    while True:
        inp = input("Search for (q for exit): ")

        if not inp:
            print("Please provide a search term")
        elif inp == "q":
            print("Bye")
            break
        else:
            filtered = []
            for e in entries:
                if filter_entries_by_tag(inp, e):
                    filtered.append(e)

            for e in sorted(filtered, key=lambda x: x.date):
                print(f"{e.date} | {e.title:80} | {e.link} | {e.tags}")

            print(f"{len(filtered)} "
                  f"{'entries' if len(filtered) != 1 else 'entry'} matched")


if __name__ == '__main__':
    main()
