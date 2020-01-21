import json


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movies_list = []
    for f in files:
        with open(f) as fp:
            movies_list.append(json.load(fp))
    return movies_list


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for m in movies:
        if "Comedy" in m["Genre"].split(", "):
            return m["Title"]


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    return max(movies,
               key=lambda m: int(m["Awards"].split(" & ")[-1].replace(" nominations.", ""))
               )["Title"]


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    return max(movies,
               key=lambda m: int(m["Runtime"].replace(" min", ""))
               )["Title"]
