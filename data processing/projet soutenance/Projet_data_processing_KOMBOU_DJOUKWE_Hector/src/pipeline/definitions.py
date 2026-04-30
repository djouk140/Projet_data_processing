from dagster import Definitions

from .assets.extract import raw_weather_data
from .assets.transform import clean_weather_data
from .assets.load import load_weather_data

from .jobs import weather_job
from .schedules import weather_schedule

defs = Definitions(
    assets=[
        raw_weather_data,
        clean_weather_data,
        load_weather_data,
    ],
    jobs=[weather_job],
    schedules=[weather_schedule],
)