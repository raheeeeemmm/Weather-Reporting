import os
import requests
import re  # Import the regular expressions module

def is_valid_coordinate(coord):
    # Regular expression to match a valid floating-point number
    # This allows for optional sign, integer part, optional decimal part
    pattern = r'^[-+]?[0-9]*\.?[0-9]+$'
    return re.match(pattern, coord) is not None

def get_weather_data(api_key, latitude, longitude):
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        temp_kelvin = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        weather_condition = weather_data['weather'][0]['description']
        temp_celsius = temp_kelvin - 273.15
        print(f'Temperature: {temp_celsius:.2f} °C')
        print(f'Humidity: {humidity}%')
        print(f'Wind Speed: {wind_speed} m/s')
        
    else:
        print(f'Failed to retrieve data. Status Code: {response.status_code}')

# API for retrieving weather information from "OPENWEATHERMAP"
print("\nWeather Report System")
api_key = os.getenv('a23b4ffafefe3fd2f4fdaadc63c86c34', 'a23b4ffafefe3fd2f4fdaadc63c86c34')

ch = int(input("\nWhich City\n1. ISLAMABAD\n2. RAWALPINDI\nEnter Your Choice: "))
if ch == 1:
    print("\nIslamabad Weather => \n")
    latitude = 33.6844
    longitude = 73.0479
    if is_valid_coordinate(str(latitude)) and is_valid_coordinate(str(longitude)):
        get_weather_data(api_key, latitude, longitude)
elif ch == 2:
    print("\nRawalpindi Weather => \n")
    latitude = 33.5651
    longitude = 73.0169
    if is_valid_coordinate(str(latitude)) and is_valid_coordinate(str(longitude)):
        get_weather_data(api_key, latitude, longitude)
