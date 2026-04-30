# resources.py
import requests
from dagster import resource

@resource
def api_resource():
    return {
        "url": "https://api.open-meteo.com/v1/forecast"
    }