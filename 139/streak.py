from datetime import datetime, timedelta, date
import re

TODAY = date(2018, 11, 12)


def extract_dates(data):
    """Extract unique dates from DB table representation as shown in Bite"""
    dates = []
    r = re.findall(r"(\d{4}-\d{2}-\d{2})", data)
    for s in r:
        dt = datetime.strptime(s, "%Y-%m-%d")
        d = date(year=dt.year, month=dt.month, day=dt.day)
        if d not in dates:
            dates.append(d)

    return dates


def calculate_streak(dates):
    """Receives sequence (set) of dates and returns number of days
       on coding streak.

       Note that a coding streak is defined as consecutive days coded
       since yesterday, because today is not over yet, however if today
       was coded, it counts too of course.

       So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
       the table makes for a 3 days coding streak.

       See the tests for more examples that will be used to pass your code.
    """
    day_earlier = None
    max_streak = 0
    streak = 0
    for d in sorted(dates, reverse=True):
        if not day_earlier:
            if d < TODAY - timedelta(1):
                return 0
            else:
                day_earlier = TODAY
        if d == day_earlier - timedelta(1) or d == day_earlier:
            streak += 1
            if streak >= max_streak:
                max_streak = streak
        else:
            streak = 0
        day_earlier = d

    return max_streak
