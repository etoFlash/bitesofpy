from urllib.request import urlretrieve
from pathlib import Path
import re

import gender_guesser.detector as gender
from bs4 import BeautifulSoup as Soup

TMP = Path('/tmp')
PYCON_HTML = TMP / "pycon2019.html"
PYCON_PAGE = ('https://bites-data.s3.us-east-2.amazonaws.com/'
              'pycon2019.html')

if not PYCON_HTML.exists():
    urlretrieve(PYCON_PAGE, PYCON_HTML)


def _get_soup(html=PYCON_HTML):
    return Soup(html.read_text(encoding="utf-8"), "html.parser")


def get_pycon_speaker_first_names(soup=None):
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
       speakers (class "speaker"). Note that some items contain
       multiple speakers so you need to extract them.
       Return a list of first names
    """
    if not soup:
        soup = _get_soup()

    speakers = []
    for s in soup.select("span.speaker"):
        for speaker in re.split(r"[,/] ", s.getText()):
            speakers.append(speaker.split()[0])

    return speakers


def get_percentage_of_female_speakers(first_names):
    """Run gender_guesser on the names returning a percentage
       of female speakers (female and mostly_female),
       rounded to 2 decimal places."""
    d = gender.Detector()
    female_counter = 0

    for name in first_names:
        if d.get_gender(name) in ("female", "mostly_female"):
            female_counter += 1

    return round(female_counter / len(first_names) * 100, 2)


if __name__ == '__main__':
    names = get_pycon_speaker_first_names()
    perc = get_percentage_of_female_speakers(names)
    print(perc)
