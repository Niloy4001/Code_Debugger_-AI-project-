import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=key)


def issue_generator(images,soln_type):
    if soln_type == "Hints":
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=[images,"give me step by step hints to solve the issue.don't give code. make sure you provided with proper markdown"]
        )
        return (response.text)

    else:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=[images," give me step by step hints to solve the issue with corrected code. make sure you provided with proper markdown"]
        )
        return (response.text)


