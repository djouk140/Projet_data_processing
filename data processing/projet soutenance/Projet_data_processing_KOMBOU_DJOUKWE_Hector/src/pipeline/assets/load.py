import psycopg2
from dagster import asset

@asset
def load_weather_data(clean_weather_data):
    conn = psycopg2.connect(
        host="postgres",
        dbname="pipeline_db",
        user="user",
        password="password"
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            temp FLOAT,
            wind FLOAT
        )
    """)

    cur.execute(
        "INSERT INTO weather VALUES (%s, %s)",
        (clean_weather_data["temp"], clean_weather_data["wind"])
    )

    conn.commit()
    conn.close()