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
Blog = namedtuple('Blog', blog.keys())


def dict2nt(dict_):
    return Blog(**dict_)


def nt2json(nt):
    nt = nt._replace(started=str(nt.started))
    return json.dumps(nt._asdict())
