import streamlit as st
import requests
import pickle
import streamlit_authenticator as stauth
from pathlib import Path

st.set_page_config(page_title='Weather App', page_icon="⛅")

API_KEY = "b99b652d448e47e5a48a226c5ed84910"

# Function to fetch weather data
def get_weather(location):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

# Authentication

names = ["Yuvraj", "Kanishq"];
users = ['yuvraj88', 'kanishq55'];
password = ['Yuvraj123', 'Kanishq123'];

hashed_passwords = stauth.Hasher(password).generate();

file_path = Path(__file__).parent/'hashed_pass.pkl';

with file_path.open('wb') as file:
  pickle.dump(hashed_passwords, file);


# Load hashed passwords
file_path = Path(__file__).parent / 'hashed_pass.pkl'
with file_path.open('rb') as file:
    hashed_pass = pickle.load(file)

credentials = {"usernames": {}}
for user, name, pwd in zip(users, names, hashed_pass):
    user_dict = {"name": name, "password": pwd}
    credentials["usernames"].update({user: user_dict})

# Authentication object creation
authenticator = stauth.Authenticate(credentials, "weather_auth", "xyzabc", cookie_expiry_days=30)

# Corrected login process
name, authentication_status, _ = authenticator.login("main", "login")  # Ignoring third value (_)

if authentication_status == False:
    st.error("Incorrect username or password!!")
elif authentication_status == None:
    st.warning("Please enter username and password!!")
elif authentication_status == True:
    st.title("Weather App")
    authenticator.logout("Log Out", "main")
    st.markdown(f'##Welcom {name}')

    location = st.text_input("Enter the name of the city:")

    if st.button("Get Weather"):
        if location:
            data = get_weather(location)
            if data.get("cod") != 200:
                st.error(data.get("message", "An error occurred."))
            else:
                st.success(f"Weather in {data['name']}, {data['sys']['country']}:")
                st.write(f"Temperature: {data['main']['temp']}°C")
                st.write(f"Condition: {data['weather'][0]['description']}")
                st.write(f"Wind: {data['wind']['speed']} kph")
                st.write(f"Humidity: {data['main']['humidity']}%")
        else:
            st.warning("Please enter a location.")
