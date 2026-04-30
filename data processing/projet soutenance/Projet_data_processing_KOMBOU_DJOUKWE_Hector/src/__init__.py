# __init__.py
from dagster import Definitions
from .assets import extract, transform, load
from .jobs import weather_job
from .schedules import daily_schedule

defs = Definitions(
    assets=[extract.raw_weather, transform.clean_weather, load.stored_weather],
    jobs=[weather_job],
    schedules=[daily_schedule]
)