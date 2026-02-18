import streamlit as st
from google import genai
st.text_input("List of ingredients goes here")
st.button("cook")

import time
def cook_food(prompt):
    if prompt:
        msg = st.toast("Gathering ingredients...")
        time.sleep(2)
        msg = st.toast("Cooking...")
        time.sleep(2)
        msg = st.toast("Ready!", icon="🥞")
        time.sleep(2)
        st.write(f"So you want to prepare {prompt} today.")
        time.sleep(1)
        st.write("Let's see how you can make it.")
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=f"Write a summarized recipe on {prompt}")
        st.write(response.text)

# a function to pull up images goes here
# I will write this function later 

if __name__=="__main__":
    API_KEY = "AIzaSyA6CU4FLXqvIgktdBQYoCf-f1YmFcEedJY"   # YOUR API
    # initialize the client
    client = genai.Client(api_key="AIzaSyA6CU4FLXqvIgktdBQYoCf-f1YmFcEedJY")
    # title 
    st.title("Recipe Generator")
    prompt = st.chat_input("What's cooking?")
    cook_food(prompt)