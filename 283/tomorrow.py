from datetime import date, timedelta


def tomorrow(today=None):
    return (today or date.today()) + timedelta(1)
