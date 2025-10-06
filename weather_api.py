import requests
import os
from dotenv import load_dotenv

load_dotenv()
WEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city: str):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url).json()

    if "list" not in response:
        raise ValueError(f"Error fetching weather: {response}")

    forecast = response["list"][8]  # ~24 hours ahead
    condition = forecast["weather"][0]["main"]
    temp = forecast["main"]["temp"]

    return {"condition": condition, "temp": temp}
