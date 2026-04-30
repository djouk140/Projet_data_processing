import pandas as pd
from pipeline.assets.transform import clean_weather

df = pd.DataFrame({
    "time": ["2024-01-01"],
    "temperature": [10]
})

result = clean_weather(df)

assert "day" in result.columns