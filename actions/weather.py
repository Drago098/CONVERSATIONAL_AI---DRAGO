import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    if not API_KEY:
        return "API key is missing."

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        res = requests.get(url)
        data = res.json()

        if data.get("cod") != 200:
            return f"Couldn't fetch weather for {city.title()}."

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"The current weather in {city.title()} is {desc} with {temp}°C."
    except Exception as e:
        return f"Error fetching weather: {e}"
#if __name__ == "__main__":
 ##  print(get_weather(city))