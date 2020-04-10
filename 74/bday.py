import calendar


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    day = date.weekday()
    return calendar.day_name[day]
