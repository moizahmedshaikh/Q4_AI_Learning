from litellm import completion
from dotenv import load_dotenv
import os

load_dotenv()

def openai():
    response = completion(
        model="openai/gpt-4o",
        messages=[{"role": "user", "content": "Hello, how are you?"}]
    )
    print(response)

def gemini():
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[{"role": "user", "content": "Hello, how are you?"}]
    )
    print(response)

def gemini2():
    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        messages=[{"role": "user", "content": "Hello, how are you?"}]
    )
    print(response)


openai()     