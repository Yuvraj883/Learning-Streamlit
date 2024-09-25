import streamlit as st
import requests

# Use your own OpenWeatherMap API key
API_KEY = "b99b652d448e47e5a48a226c5ed84910"  # Replace with your actual API key

# Function to fetch weather data
def get_weather(location):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"  # Added units=metric for Celsius
    response = requests.get(url)
    return response.json()

# Streamlit app layout
st.title("Weather App")
location = st.text_input("Enter a location (city name):")  # Only ask for location

if st.button("Get Weather"):
    if location:
        data = get_weather(location)
        if data.get("cod") != 200:  # Check if the API response indicates an error
            st.error(data.get("message", "An error occurred."))
        else:
            st.success(f"Weather in {data['name']}, {data['sys']['country']}:")  # Correctly accessing name and country
            st.write(f"Temperature: {data['main']['temp']}°C")  # Correct key for temperature
            st.write(f"Condition: {data['weather'][0]['description']}")  # Correct key for weather condition
            st.write(f"Wind: {data['wind']['speed']} kph")  # Correct key for wind speed
            st.write(f"Humidity: {data['main']['humidity']}%")  # Correct key for humidity
    else:
        st.warning("Please enter a location.")
