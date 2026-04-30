from dagster import ScheduleDefinition

from .jobs import weather_job

weather_schedule = ScheduleDefinition(
    job=weather_job,
    cron_schedule="0 * * * *"
)