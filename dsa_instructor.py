import streamlit as st
from google import genai
st.title("YOUR PERSONAL DSA INSTRUCTOR")
import time
def dsa_topic(prompt):
    if prompt:
        msg = st.toast("thinking...")
        time.sleep(2)
        st.write(f"Let's see about {prompt}.")
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=f"""if asked about simple data structures and algorithm and time, space complexity then answer it if asked only and give all information related to the {prompt} with simple explanation and code snippets in java also give examples and applications of {prompt}
            if the question is not related to data structures and algorithms example:"hi","how are you" or any non data structure related question then reply with "Please ask a dsa related question". Also help to 
            solve the data structure and algorithm query or problems and give the step by step approach to solve the problem and also give the code snippet in java""")
        st.write(response.text)

if __name__=="__main__":
    API_KEY = "AIzaSyBIz3ps2rJShk7eaWSMX1_9_XU2VE8RW7Y"   # YOUR API
    # initialize the client
    client = genai.Client(api_key="AIzaSyBIz3ps2rJShk7eaWSMX1_9_XU2VE8RW7Y")
    # title 
    st.header("Ask me anything about DSA")
    prompt = st.chat_input("give me the dsa topic-")
    dsa_topic(prompt)

