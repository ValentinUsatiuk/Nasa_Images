import requests
import streamlit as st

api_key = "FNnOJeWjqPhy7Y28LKJOZTGd6XTXJwGyxmv2C2te"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response1 = requests.get(url)
data = response1.json()
print(data)

title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

image_filepath = "img.png"
response2 = requests.get(image_url)
with open(image_filepath, "wb") as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)

