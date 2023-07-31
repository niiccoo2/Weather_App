import requests
import json

location = "Boston"  # replace with your desired location
api_key = "e400d74e423bf565abbc9a72c38b5e84"  # replace with your actual API key

# construct the API URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

# send the HTTP request
response = requests.get(url)

print(response.text)

# parse the JSON response data into a Python dictionary
data = json.loads(response.text)

# extract the relevant weather information from the dictionary
temperature_k = data["main"]["temp"]
temperature_min_k = data["main"]["temp_min"]
temperature_max_k = data["main"]["temp_max"]
humidity = data["main"]["humidity"]
description = data["weather"][0]["description"]


temperature_f = (temperature_k * 9/5) - 459.67
temperature_min_f = (temperature_min_k * 9/5) - 459.67
temperature_max_f = (temperature_max_k * 9/5) - 459.67


# print the weather information
print(f"The temperature in {location} is{temperature_f: .1f} degrees Fahrenheit.")
print(f"The high in {location} is{temperature_max_f: .1f} degrees Fahrenheit.")
print(f"The low in {location} is{temperature_min_f: .1f} degrees Fahrenheit.")
print(f"The humidity in {location} is {humidity}%.")
print(f"The weather in {location} is described as {description}.")