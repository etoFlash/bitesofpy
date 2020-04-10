import calendar


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    day = calendar.weekday(year=date.year, month=date.month, day=date.day)
    return calendar.day_name[day]
