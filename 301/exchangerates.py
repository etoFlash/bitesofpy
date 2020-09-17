import os
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Dict, List
from urllib.request import urlretrieve
import json

URL = "https://bites-data.s3.us-east-2.amazonaws.com/exchangerates.json"
TMP = Path(os.getenv("TMP", "/tmp"))
RATES_FILE = TMP / "exchangerates.json"

if not RATES_FILE.exists():
    urlretrieve(URL, RATES_FILE)


def get_all_days(start_date: date, end_date: date) -> List[date]:
    return [
        start_date + timedelta(i)
        for i in range((end_date - start_date).days + 1)
    ]


def match_daily_rates(start: date, end: date, daily_rates: dict) -> Dict[date, date]:
    return {
        start + timedelta(i):
            max(_str_to_date(d)
                for d in daily_rates
                if _str_to_date(d) <= (start + timedelta(i)))
        for i in range((end - start).days + 1)
    }


def _str_to_date(s: str) -> date:
    return datetime.strptime(s, "%Y-%m-%d").date()


def exchange_rates(
    start_date: str = "2020-01-01", end_date: str = "2020-09-01"
) -> Dict[date, dict]:
    with open(RATES_FILE) as f:
        dr = json.load(f)

    if start_date < dr['start_at'] or end_date > dr['end_at']:
        raise ValueError

    sd = _str_to_date(start_date)
    ed = _str_to_date(end_date)
    base_dates = match_daily_rates(sd, ed, dr['rates'])
    dr = {
        _str_to_date(k): v
        for k, v in dr['rates'].items()
    }
    result = {}

    for d in get_all_days(sd, ed):
        bd = base_dates[d]
        result[d] = {
            'Base Date': bd,
            'GBP': dr[bd]['GBP'],
            'USD': dr[bd]['USD'],
        }

    return result
