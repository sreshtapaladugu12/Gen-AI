import os
from dotenv import load_dotenv
from groq import Groq

# Load API key
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("Groq API key not found!")

# Initialize Groq client
client = Groq(api_key=api_key)

# Send prompt to AI
response = client.chat.completions.create(
  model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
           "content": "Explain the difference between AI, ML and Deep Learning with examples."
        }
    ]
)

# Display response
print("\nLLM Response:")
print(response.choices[0].message.content)