import streamlit as st
from google import genai
st.header("Poetry generator")
st.button("click")

import time
def cook_food(prompt):
    if prompt:
        msg = st.toast("thinking...")
        time.sleep(2)
        st.write("Let's see how you can make it.")
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=f"Write a poem about {prompt}")
        st.write(response.text)

# a function to pull up images goes here
# I will write this function later 

if __name__=="__main__":
    API_KEY = "AIzaSyA6CU4FLXqvIgktdBQYoCf-f1YmFcEedJY"   # YOUR API
    # initialize the client
    client = genai.Client(api_key="AIzaSyA6CU4FLXqvIgktdBQYoCf-f1YmFcEedJY")
    # title 
    st.title("poettry Generator")
    prompt = st.chat_input("give me the topic-")
    cook_food(prompt)