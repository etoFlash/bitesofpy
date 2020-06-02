from collections import namedtuple
from datetime import date

import pandas as pd

DATA_FILE = "https://bites-data.s3.us-east-2.amazonaws.com/weather-ann-arbor.csv"
STATION = namedtuple("Station", "ID Date Value")


def high_low_record_breakers_for_2015():
    """Extract the high and low record breaking temperatures for 2015

    The expected value will be a tuple with the highest and lowest record
    breaking temperatures for 2015 as compared to the temperature data
    provided.

    NOTE:
    The date values should not have any timestamps, should be a
    datetime.date() object. The temperatures in the dataset are in tenths
    of degrees Celsius, so you must divide them by 10

    Possible way to tackle this challenge:

    1. Create a DataFrame from the DATA_FILE dataset.

    2. Manipulate the data to extract the following:
       * Extract highest temperatures for each day / station pair between 2005-2015
       * Extract lowest temperatures for each  day / station  between 2005-2015
       * Remove February 29th from the dataset to work with only 365 days

    3. Separate data into two separate DataFrames:
       * high/low temperatures between 2005-2014
       * high/low temperatures for 2015

    4. Iterate over the 2005-2014 data and compare to the 2015 data:
       * For any temperature that is higher/lower in 2015 extract ID,
         Date, Value
         
    5. From the record breakers in 2015, extract the high/low of all the
       temperatures
       * Return those as STATION namedtuples, (high_2015, low_2015)
    """
    df = pd.read_csv(DATA_FILE)
    df_max = df[df["Element"] == "TMAX"].groupby(by=["ID", "Date"], as_index=False).max()
    df_min = df[df["Element"] == "TMIN"].groupby(by=["ID", "Date"], as_index=False).min()
    h15 = df_min[df_min["Date"] >= "2015-01-01"]

    first_id = h15.iloc[0]["ID"]
    result_min = []
    for row in h15[h15["ID"] == first_id].iterrows():
        r = row[1]
        _, md = r["Date"].split("-", 1)
        r_max_15 = h15[h15["Date"] == f"2015-{md}"].sort_values(by="Data_Value").head(1).iloc[0]
        min_val_15 = r_max_15["Data_Value"]
        min_id_15 = r_max_15["ID"]

        if md == "05-09":
            continue

        values = []
        for y in range(2005, 2015):
            values.append(df_min[(df_min["Date"] == f"{y}-{md}")]["Data_Value"].min())

        if min_val_15 < min(values):
            result_min.append(STATION(min_id_15,
                                      date(*map(int, f"2015-{md}".split("-"))),
                                      min_val_15 / 10))

    h15 = df_max[df_max["Date"] >= "2015-01-01"]
    result_max = []
    for row in h15[h15["ID"] == first_id].iterrows():
        r = row[1]
        _, md = r["Date"].split("-", 1)
        r_max_15 = h15[h15["Date"] == f"2015-{md}"].sort_values(by="Data_Value", ascending=False).head(1).iloc[0]
        max_val_15 = r_max_15["Data_Value"]
        max_id_15 = r_max_15["ID"]

        if md == "05-09":
            continue

        values = []
        for y in range(2005, 2015):
            values.append(df_max[(df_max["Date"] == f"{y}-{md}")]["Data_Value"].max())

        if max_val_15 > max(values):
            result_max.append(STATION(max_id_15,
                                      date(*map(int, f"2015-{md}".split("-"))),
                                      max_val_15 / 10))

    return (
        max(result_max, key=lambda x: x.Value),
        min(result_min, key=lambda x: x.Value),
    )
