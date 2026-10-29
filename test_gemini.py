from dotenv import load_dotenv
from google import genai
from google.genai import types
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
    http_options=types.HttpOptions(timeout=120000)
)

print("Testing Gemini 3.6 Flash...")

try:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Generate one short SOC Analyst interview question.",
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(
                thinking_level="low"
            ),
            max_output_tokens=512
        )
    )

    print("Response text:", repr(response.text))
    print("Candidates:", response.candidates)

except Exception as error:
    print("Gemini request failed:")
    print(type(error).__name__, str(error))
