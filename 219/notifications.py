from datetime import date, timedelta

TODAY = date.today()


def gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY):
    days_step = timedelta(num_days)
    dt = start_date
    while True:
        dt += days_step
        for _ in range(num_bites):
            yield dt
