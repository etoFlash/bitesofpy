"""Checks community branch dir structure to see who submitted most
   and what challenge is more popular by number of PRs"""
from collections import Counter, namedtuple
import os
import urllib.request
import re

# prep
temp_file = os.path.join('/tmp', 'dir_names')
urllib.request.urlretrieve('http://bit.ly/2ABUTjv', temp_file)

IGNORE = 'static templates data pybites bbelderbos hobojoe1848'.split()

users, popular_challenges = Counter(), Counter()

Stats = namedtuple('Stats', 'user challenge')


# code

def gen_files():
    """Return a generator of dir names reading in temp_file

       temp_file has this format:

       challenge<int>/file_or_dir<str>,is_dir<bool>
       03/rss.xml,False
       03/tags.html,False
       ...
       03/mridubhatnagar,True
       03/aleksandarknezevic,True

       -> use last column to filter out directories (= True)
    """
    with open(temp_file, "r") as f:
        for line in f:
            if line.endswith(",False\n"):
                continue
            yield line


def diehard_pybites():
    """Return a Stats namedtuple (defined above) that contains the user that
       made the most PRs (ignoring the users in IGNORE) and a challenge tuple
       of most popular challenge and the amount of PRs for that challenge.
       Calling this function on the dataset (held temp_file) should return:
       Stats(user='clamytoe', challenge=('01', 7))
    """
    for file in gen_files():
        challenge, user = re.search(r"(.*?)/(.*?),", file).groups()
        if user in IGNORE:
            continue
        users[user] += 1
        popular_challenges[challenge] += 1
    return Stats(users.most_common(1)[0][0],
                 *popular_challenges.most_common(1))
