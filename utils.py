from google import genai 
from google.genai import types

def call_gemini(history):
    client = genai.Client()
    return client.models.generate_content(
            model="gemini-2.5-flash", contents=f"{history}", config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
    )
            ).text


