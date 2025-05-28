# First OpenAI API Call

A simple Python application that demonstrates how to make API calls to OpenAI's GPT models using the OpenAI Python client library.

## Description

This project provides a basic implementation of interacting with OpenAI's API. It allows users to:

- Input a message via the command line
- Send the message to OpenAI's GPT-3.5-turbo model
- Receive and display the AI's response
- View token usage statistics

## Requirements

- Python 3.6+
- OpenAI Python library (v1.0.0 or later)
- python-dotenv

## Installation

1. Clone this repository:
   ```
   git clone <repository-url>
   cd first-openai-api-call
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the script with Python:

```
python first_call.py
```

When prompted, enter your message. The application will send your message to the OpenAI API and display the response along with token usage information.

## Project Structure

- `first_call.py` - Main script that handles the API interaction
- `requirements.txt` - Lists the project dependencies
- `.env` - Contains your OpenAI API key (not tracked by git)
- `.gitignore` - Configured to ignore the .env file for security

## Security Note

This project uses a `.env` file to store your OpenAI API key. This file is included in `.gitignore` to prevent accidentally committing your API key to version control.
