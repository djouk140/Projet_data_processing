import pandas as pd
from dagster import asset

@asset
def clean_weather(raw_weather):
    df = raw_weather.copy()

    df["time"] = pd.to_datetime(df["time"])
    df["day"] = df["time"].dt.date

    return df