import os
import urllib.request
from collections import Counter

# data provided
stopwords_file = os.path.join('/tmp', 'stopwords')
harry_text = os.path.join('/tmp', 'harry')
urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)


def get_harry_most_common_word():
    words = []

    with open(stopwords_file) as f:
        stopwords = [w.strip() for w in f.readlines()]

    with open(harry_text) as f:
        for line in f:
            for w in line.split():
                word = "".join(c.lower() for c in w if c.isalnum())
                if word and word not in stopwords:
                    words.append(word)

    return Counter(words).most_common(1)[0]
