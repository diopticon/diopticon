# app/main.py

import streamlit as st
import os
from langchain.llms import OpenAI

# Load environment variables (for OpenAI API key)
if os.path.exists('.env'):
    from dotenv import load_dotenv
    load_dotenv()

OPENAI_API = os.getenv("OPENAI_API")

# Initialize LLMS (Language Model)
llm = OpenAI(api_key=OPENAI_API)

# Streamlit app
st.title("Simple Chat Interface")

# Chatbot functionality
user_input = st.text_input("Your Message")
if user_input:
    # Send user input to the chatbot model and get response
    response = llm.generate(prompt=user_input, max_length=50)

    # Display the chatbot's response
    st.text_area("Chatbot Response", response)
