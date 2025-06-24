import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load .env variables
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Create new genai client
client = genai.Client(api_key=api_key)

# Get the prompt from sys.argv
if len(sys.argv) < 2:
    print("Usage: python3 main.py <prompt to gemini> [--verbose (optional)]")
    sys.exit(1)
user_prompt = sys.argv[1]

verboseFlag = False
if len(sys.argv) == 3:
    verboseFlag = True

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)])
]

response = client.models.generate_content(
    model='gemini-2.0-flash-001', 
    contents=messages,
)
if verboseFlag:
    print(f"User prompt: {response.text}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
