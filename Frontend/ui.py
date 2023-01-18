import streamlit as st
import httpx
import json
from PIL import Image

st.title("CoCe :robot_face:")

def classify(filepath):
    response = httpx.post(url = "http://backend:8080/classify", data = json.dumps({"filepath": filepath}))
    result = response.json()
    return result["prediction"]

option = st.selectbox(label = "Please select an image for classification from the list below:", options = ("Airplane #1", "Airplane #2", "Airplane #3", 
"Airplane #4", "Automobile #1", "Automobile #2", "Automobile #3", "Automobile #4", "Bird #1", "Bird #2", 
"Cat #1", "Cat #2", "Deer #1", "Deer #2", "Dog #1", "Dog #2", "Frog #1", "Frog #2", "Frog #3",
"Horse #1", "Horse #2", "Horse #3", "Horse #4", "Ship #1", "Ship #2", "Truck #1", "Truck #2", "Truck #3"))

image = Image.open(fp = "images/"+option+".jpg")
st.image(image = image)

if st.button(label = "Classify"):
    st.info(body = "CoCe's prediction: " + classify(filepath = "images/"+option+".jpg"))