import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# System and user messages
system_prompt = {"role": "system", "content": "You are a helpful assistant."}
user_input = input("Enter your message: ")
user_prompt = {"role": "user", "content": user_input}

# Make the API call
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[system_prompt, user_prompt]
)

# Extract and print assistant response
reply = response.choices[0].message.content
print("\nAssistant Response:\n", reply)

# Print token usage
usage = response.usage
print("\nToken Usage:")
print(f"Prompt Tokens: {usage.prompt_tokens}")
print(f"Completion Tokens: {usage.completion_tokens}")
print(f"Total Tokens: {usage.total_tokens}")