from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    last_day_year_counter = PYBITES_BORN
    last_day_hundred_days_counter = PYBITES_BORN
    year_delta = timedelta(days=365)
    hundred_days_delta = timedelta(days=100)
    while True:
        if last_day_year_counter + year_delta < last_day_hundred_days_counter + hundred_days_delta:
            last_day_year_counter += year_delta
            yield last_day_year_counter
        else:
            last_day_hundred_days_counter += hundred_days_delta
            yield last_day_hundred_days_counter
