import requests

def fetch_weather_data(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change this to "imperial" for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    return weather_data

def display_weather_data(weather_data):
    print("Weather in", weather_data["name"])
    print("Temperature:", weather_data["main"]["temp"], "°C")
    print("Description:", weather_data["weather"][0]["description"])

if __name__ == "__main__":
    # Replace "YOUR_API_KEY_HERE" with your actual OpenWeatherMap API key
    api_key = "YOUR_API_KEY_HERE"
    city = input("Enter city name: ")
    weather_data = fetch_weather_data(api_key, city)
    if "cod" in weather_data and weather_data["cod"] == 200:
        display_weather_data(weather_data)
    else:
        print("City not found or error fetching weather data.")
