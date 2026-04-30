import requests
from voice.tts import say
from config.settings import WEATHER_API_KEY

def get_weather():
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    try:
        ip_data = requests.get("http://ip-api.com/json/").json()
        city = ip_data.get("city")
        country = ip_data.get("countryCode")
        location = f"{city},{country}"
    except:
        location = "Lucknow,IN"

    url = f"{base_url}q={location}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") == 200:
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        say(f"Temperature is {temp}°C with {desc}")
    else:
        say("Unable to fetch weather")
