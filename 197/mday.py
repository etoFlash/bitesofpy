from dateutil.rrule import *
from datetime import date


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    return rrule(
        DAILY, count=2, dtstart=date(year=year, month=5, day=1), byweekday=SU
    )[1].date()
