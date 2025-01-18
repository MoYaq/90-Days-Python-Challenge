#Day 13: Using External Libraries – Requests
#Project: Fetch and Display Weather Data from a Public API
#A project to demonstrate how to use the requests library to make HTTP requests and retrieve data from an API.

#Step 1: Install the requests library
#In Replit, install requests by running: pip install requests (if you are coding with your phone)
pip install requests

#Step 2: Import the library
import requests

#Step 3: Define a function to fetch weather data
def get_weather(city):
    api_key = "20d100de54e13b67f02ea38203b7b283" 
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric" #Use "imperial" for Fahrenheit
    }
    
#Raise an error for bad responses (4xx or 5xx)
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

#Convert the response to JSON format
        data = response.json()
        
#Extract useful weather details
        temperature = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        city_name = data["name"]
        country = data["sys"]["country"]

        print(f"\nWeather in {city_name}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {weather_desc.capitalize()}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    except KeyError:
        print("Invalid response. Please check the city name and try again.")

#Step 4: Main Program
if __name__ == "__main__":
    print("Welcome to the Weather App! 🌤️")
    
    while True:
        city = input("\nEnter the name of a city to get the weather (or type 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("Cheeriooo👋")
            break
        get_weather(city)