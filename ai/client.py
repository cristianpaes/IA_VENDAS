import os
from google import genai

try:
    import streamlit as st

    if hasattr(st, "secrets") and "GEMINI_API_KEY" in st.secrets:
        api_key = st.secrets["GEMINI_API_KEY"]
    else:
        raise Exception()

except:

    from dotenv import load_dotenv

    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)