import streamlit as st
from google import genai
st.header("Story generator")

st.button("click to get story")

import time
def cook_food(prompt):
    if prompt:
        msg = st.toast("Generating story...")
        time.sleep(2)
        msg = st.toast("Ready!")
        time.sleep(2)
        st.write(f"So you want the story {prompt}")
        time.sleep(1)
        st.write("Let's see how you can make it.")
        author = "Ruskin Bond"
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=f"Write a summarized story about {prompt} by {author}")
        st.write(response.text)

# a function to pull up images goes here
# I will write this function later 

if __name__=="__main__":
    API_KEY = "AIzaSyA6CU4FLXqvIgktdBQYoCf-f1YmFcEedJY"   # YOUR API
    # initialize the client
    client = genai.Client(api_key="AIzaSyA6CU4FLXqvIgktdBQYoCf-f1YmFcEedJY")
    # title 
    st.title("Story Generator")
    prompt = st.chat_input("What's the story about?")
    cook_food(prompt)
