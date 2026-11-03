import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

print("1. Loading API key...", flush=True)

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found in .env")

print("2. Connecting to Gemini...", flush=True)

client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(timeout=60000)
)

print("3. Sending request...", flush=True)

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents="say hello in one sentence"
    )

    print("\n4. Gemini response:", flush=True)
    print(response.text, flush=True)

except Exception as e:
    print("\nRequest failed:", str(e), flush=True)