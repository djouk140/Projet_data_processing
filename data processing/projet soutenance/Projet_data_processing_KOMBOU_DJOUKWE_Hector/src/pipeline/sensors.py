from dagster import sensor, RunRequest
from .jobs import weather_job

@sensor(job=weather_job)
def api_sensor(context):
    yield RunRequest(run_key=None)