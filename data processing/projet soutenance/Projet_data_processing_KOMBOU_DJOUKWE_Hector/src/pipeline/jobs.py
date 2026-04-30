from dagster import define_asset_job

weather_job = define_asset_job(
    name="weather_job"
)