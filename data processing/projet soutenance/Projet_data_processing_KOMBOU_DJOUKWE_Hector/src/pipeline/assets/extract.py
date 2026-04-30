import requests
from dagster import asset

@asset
def raw_weather_data():
    url = "https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&current_weather=true"
    return requests.get(url).json()