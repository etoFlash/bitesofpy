from pathlib import Path
from urllib.request import urlretrieve

import pytest

from omdb import (get_movie_data,
                  get_single_comedy,
                  get_movie_most_nominations,
                  get_movie_longest_runtime)

TMP = Path('/tmp')
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DATA = 'omdb_data'

DATA_LOCAL = TMP / DATA
if not Path(DATA_LOCAL).exists():
    urlretrieve(S3 + DATA, DATA_LOCAL)


@pytest.fixture(scope="module")
def movies():
    files = []
    with open(DATA_LOCAL) as f:
        for i, line in enumerate(f.readlines(), 1):
            movie_json = TMP / f'{i}.json'
            with open(movie_json, 'w') as f:
                f.write(f'{line}\n')
            files.append(movie_json)

    yield get_movie_data(files)

    # teardown
    for file_ in files:
        file_.unlink()


def test_len_movie_data(movies):
    assert len(movies) == 5


def test_type_of_movie_elements(movies):
    assert all(type(m) == dict for m in movies)


@pytest.mark.parametrize("func, expected", [
    (get_single_comedy, 'Horrible Bosses'),
    (get_movie_most_nominations, 'Fight Club'),
    (get_movie_longest_runtime, 'Blade Runner 2049'),
])
def test_data_analysis(func, expected, movies):
    assert func(movies) == expected