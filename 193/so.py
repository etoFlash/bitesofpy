import requests
from bs4 import BeautifulSoup

cached_so_url = 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'


def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    r = requests.get(cached_so_url)
    r.raise_for_status()
    s = BeautifulSoup(r.text, "html.parser")
    top = []
    for q in s.select("div#questions div.question-summary"):
        if not q.select_one("div.views").getText().strip().endswith("m views"):
            continue
        top.append(
            (q.select_one("a.question-hyperlink").getText(),
             int(q.select_one("span.vote-count-post").getText()))
        )

    return sorted(top,
                  key=lambda x: x[1],
                  reverse=True)
