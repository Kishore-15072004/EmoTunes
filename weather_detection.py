import requests

def classify_weather(weather_desc):
    """
    Classify the weather description into categories like 'sunny', 'cloudy', or 'rainy'.
    
    :param weather_desc: Description of the current weather.
    :return: Categorized weather condition.
    """
    weather_desc = weather_desc.lower()
    if any(keyword in weather_desc for keyword in ["clear", "sunny", "partly cloudy", "mostly sunny"]):
        return "sunny"
    elif any(keyword in weather_desc for keyword in ["cloudy", "mostly cloudy", "overcast", "fog", "foggy", "haze", "mist"]):
        return "cloudy"
    elif any(keyword in weather_desc for keyword in ["drizzle", "showers", "rain", "heavy rain", "thunderstorms", "sleet", "hail", "snow", "snow showers", "flurries", "blizzard"]):
        return "rainy"
    else:
        return "cloudy"

def get_weather():
    """
    Fetch the current weather information using the user's IP location and classify the weather.
    
    :return: Categorized weather condition.
    """
    api_key = "97b8e6665b7c483d3420767e03d09215"  # Your OpenWeatherMap API key
    try:
        res = requests.get('https://ipinfo.io/')
        res.raise_for_status()
        data = res.json()

        loc = data['loc'].split(',')
        lat, lon = loc[0], loc[1]
        url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
        res = requests.get(url)
        res.raise_for_status()
        weather_data = res.json()

        weather_desc = weather_data['weather'][0]['description']

        return classify_weather(weather_desc)
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return "unknown"

# Example usage for testing
if __name__ == "__main__":
    classified_weather = get_weather()
    print(f"Classified Weather: {classified_weather}")
