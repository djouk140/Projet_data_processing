import pandas as pd
from pipeline.assets.transform import clean_weather


def test_transform():
    data = {
        "current_weather": {
            "temperature": 20,
            "windspeed": 5
        }
    }

    result = clean_weather_data(data)

    assert result["temp"] == 20
    assert result["wind"] == 5