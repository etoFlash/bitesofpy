import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve
from statistics import mean

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movies_by_director = defaultdict(list)

    with open(MOVIE_DATA, "r", encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if not row["title_year"]:
                continue
            year = int(row["title_year"])
            if year < 1960:
                continue
            director_name = row["director_name"]
            title = row["movie_title"].strip()
            score = float(row["imdb_score"])
            movies_by_director[director_name].append(Movie(title=title, year=year, score=score))

    return movies_by_director


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    return round(mean(m.score for m in movies), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    average_scores = []

    for director, movies in directors.items():
        if len(movies) < MIN_MOVIES:
            continue
        average_scores.append((director, calc_mean_score(movies)))

    return sorted(average_scores,
                  key=lambda t: t[1],
                  reverse=True)
