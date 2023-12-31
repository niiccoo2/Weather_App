import requests
import json
import tkinter as tk
from PIL import ImageTk, Image

#global current_unit
current_unit = "F"
def get_weather():
    global current_unit
    location = location_entry.get() # Retrieve the location from the entry field
    api_key = "e400d74e423bf565abbc9a72c38b5e84"  # replace with your actual API key

    # construct the API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

    try:
        # send the HTTP request
        response = requests.get(url)
        response.raise_for_status()  # raise an exception if the HTTP request fails

        # parse the JSON response data into a Python dictionary
        data = json.loads(response.text)

        # extract the relevant weather information from the dictionary
        temperature_k = data["main"]["temp"]
        temperature_min_k = data["main"]["temp_min"]
        temperature_max_k = data["main"]["temp_max"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        if current_unit == "F":
            temperature_f = (temperature_k * 9/5) - 459.67
            temperature_min_f = (temperature_min_k * 9/5) - 459.67
            temperature_max_f = (temperature_max_k * 9/5) - 459.67

            temperature_label.config(text=f"Temperature: {temperature_f:.1f}°F")
            high_label.config(text=f"High: {temperature_max_f:.1f}°F")
            low_label.config(text=f"Low: {temperature_min_f:.1f}°F")
        else:
            temperature_c = temperature_k - 273.15
            temperature_min_c = temperature_min_k - 273.15
            temperature_max_c = temperature_max_k - 273.15

            temperature_label.config(text=f"Temperature: {temperature_c:.1f}°C")
            high_label.config(text=f"High: {temperature_max_c:.1f}°C")
            low_label.config(text=f"Low: {temperature_min_c:.1f}°C")
        humidity_label.config(text=f"Humidity: {humidity}%")
        description_label.config(text=f"Description: {description.capitalize()}")

    except requests.exceptions.HTTPError as e:
        # handle HTTP errors
        temperature_label.config(text="Temperature: N/A")
        high_label.config(text="High: N/A")
        low_label.config(text="Low: N/A")
        humidity_label.config(text="Humidity: N/A")
        description_label.config(text=f"Error: {e}")

    except (KeyError, json.JSONDecodeError) as e:
        # handle JSON parsing errors
        temperature_label.config(text="Temperature: N/A")
        high_label.config(text="High: N/A")
        low_label.config(text="Low: N/A")
        humidity_label.config(text="Humidity: N/A")
        description_label.config(text=f"Error: Invalid location or API key")

def change_units():
    global current_unit
    if current_unit == "F":
        current_unit = "C"
    else:
        current_unit = "F"
    get_weather()

# print the weather information
#print(f"The temperature in {location} is{temperature_f: .1f} degrees Fahrenheit.")
#print(f"The high in {location} is{temperature_max_f: .1f} degrees Fahrenheit.")
#print(f"The low in {location} is{temperature_min_f: .1f} degrees Fahrenheit.")
#print(f"The humidity in {location} is {humidity}%.")
#print(f"The weather in {location} is described as {description}.")

root = tk.Tk()
root.title("Nico's Weather App")
root.configure(bg='#859DEB')

#img = Image.open("C:/Users/Nico/Documents/Python/Weather/download.ico") # For laptop
img = Image.open("C:/Users/nicos/Documents/Python/Weather/Weather_App/download.ico") # For PC
icon = ImageTk.PhotoImage(img)
root.iconphoto(True, icon)

location_label = tk.Label(root, text="Enter location:")
location_entry = tk.Entry(root)
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
change_unit = tk.Button(root, text="Change Units", command=change_units)
temperature_label = tk.Label(root, text="Temperature: ")
high_label = tk.Label(root, text="High: ")
low_label = tk.Label(root, text="Low: ")
humidity_label = tk.Label(root, text="Humidity: ")
description_label = tk.Label(root, text="Description: ")

location_label.grid(row=0, column=0, padx=10, pady=10)
location_entry.grid(row=0, column=1, padx=10, pady=10)
get_weather_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
change_unit.grid(row=1, column=2, columnspan=2, padx=10, pady=10)
temperature_label.grid(row=2, column=0, padx=10, pady=10)
high_label.grid(row=3, column=0, padx=10, pady=10)
low_label.grid(row=4, column=0, padx=10, pady=10)
humidity_label.grid(row=5, column=0, padx=10, pady=10)
description_label.grid(row=6, column=0, padx=10, pady=10)

root.mainloop()