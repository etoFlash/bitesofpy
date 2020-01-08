from collections import namedtuple
from datetime import datetime
import json


blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here
Blog = namedtuple('Blog', 'name, founders, started, tags, location, site')


def dict2nt(dict_):
    return Blog(**dict_)


def nt2json(nt):
    result = dict()
    for key, value in nt._asdict().items():
        if type(value) == datetime:
            result[key] = str(value)
        else:
            result[key] = value

    return json.dumps(result)
