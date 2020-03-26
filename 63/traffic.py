from collections import namedtuple
from itertools import cycle, islice
from time import sleep

State = namedtuple('State', 'color command timeout')


def traffic_light():
    """Returns an itertools.cycle iterator that
       when iterated over returns State namedtuples
       as shown in the Bite's description"""
    states = cycle([State(color='red', command='Stop', timeout=2),
                    State(color='green', command='Go', timeout=2),
                    State(color='amber', command='Caution', timeout=0.5)])
    for state in states:
        yield state


if __name__ == '__main__':
    # print a sample of 10 states if run as standalone program
    for state in islice(traffic_light(), 10):
        print(f'{state.command}! The light is {state.color}')
        sleep(state.timeout)
