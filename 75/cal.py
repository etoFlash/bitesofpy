def get_weekdays(calendar_output):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    week_day_names = []
    weeks = {}
    for w in calendar_output.splitlines()[1:]:
        if not week_day_names:
            week_day_names = w.split()
            continue
        week_days = [int(d) for d in w.split()]
        if len(week_days) == 7:
            week = zip(week_days, week_day_names)
        elif not weeks:
            week = zip(week_days, week_day_names[-len(week_days):])
        else:
            week = zip(week_days, week_day_names[:len(week_days)])
        weeks.update(dict(week))

    return weeks
