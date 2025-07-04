import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.call_function import call_function, available_functions
from prompts import system_prompt
from config import MAX_ITERS


def main():
    # Load .env variables
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # Create new genai client
    client = genai.Client(api_key=api_key)

    # Get the prompt from sys.argv
    if len(sys.argv) < 2:
        print('Usage: uv run main.py "Your prompt here" [--verbose]')
        sys.exit(1)
    user_prompt = sys.argv[1]
    verboseFlag = "--verbose" in sys.argv

    if verboseFlag:
        print(f"User prompt: {user_prompt}\n")

    

    # Create obj for handling conversation context
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    for i in range(0, MAX_ITERS):
        # Make a call to the AI and get response
        response = client.models.generate_content(
            model='gemini-2.0-flash-001', 
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], 
                system_instruction=system_prompt
                )
        )
        # Check for response candidates. If so, add each of them to messages
        if len(response.candidates) > 0:
            for candidate in response.candidates:
                # Add the response candidates to messages
                messages.append(candidate.content)
        
        # Check if agent made function calls, print them if so and loop again. Otherwise, print response text and break.
        if response.function_calls:
            function_call_results = [
                call_function(function_call_part, verbose=verboseFlag)
                for function_call_part in response.function_calls
            ]
            messages.extend(function_call_results)
            for function_call_result in function_call_results:
                if function_call_result.parts[0].function_response.response:
                    if verboseFlag:
                        print(f"-> {function_call_result.parts[0].function_response.response}")
                else:
                    raise Exception(f'Error getting response from function: {function_call_part.name}')
        else:
            print(f"Response: {response.text}")
            break

    if verboseFlag: 
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
