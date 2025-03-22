import streamlit as st
import requests
import matplotlib.pyplot as plt

# Title of the app
st.title("🌤️ Interactive Weather Dashboard")

# API Key and Base URL for OpenWeatherMap
API_KEY = "your_openweathermap_api_key"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# User input for city name
city = st.text_input("Enter a city name", "New York")

# Fetch weather data
if st.button("Get Weather"):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Fetch temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()

        # Extract weather details
        weather = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Display weather details
        st.subheader(f"Weather in {city}")
        st.write(f"**Condition:** {weather}")
        st.write(f"**Temperature:** {temp}°C")
        st.write(f"**Feels Like:** {feels_like}°C")
        st.write(f"**Humidity:** {humidity}%")
        st.write(f"**Wind Speed:** {wind_speed} m/s")

        # Visualization: Temperature and Humidity
        fig, ax = plt.subplots(figsize=(6, 4))
        labels = ["Temperature", "Feels Like", "Humidity"]
        values = [temp, feels_like, humidity]
        ax.bar(labels, values, color=["skyblue", "orange", "green"])
        ax.set_title(f"Weather Metrics for {city}")
        ax.set_ylabel("Value")
        st.pyplot(fig)
    else:
        st.error("City not found. Please enter a valid city name.")