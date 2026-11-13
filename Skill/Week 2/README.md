# Week 2 – Provider-Agnostic LLM Client

## Project Description
This project implements a provider-agnostic Large Language Model (LLM) client that supports two AI providers through a common interface.

The application supports:
- **Gemini:** Cloud-based AI model using Google GenAI API.
- **Ollama:** Local AI model using Llama 3.2.

## Technologies Used
- Python
- Google GenAI
- Ollama
- Llama 3.2
- Requests
- Python-dotenv
- Unittest

## Project Structure
```text
week-2/
│
├── llm_client.py
├── main.py
├── test_client.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Features
1. Supports multiple LLM providers.
2. Uses a common interface for different AI models.
3. Allows users to select Gemini or Ollama.
4. Generates responses based on user prompts.
5. Includes unit testing using Python unittest.

## Installation and Setup

1. Install Python.
2. Install Ollama from https://ollama.com/download
3. Download the Llama 3.2 model:

```bash
ollama pull llama3.2
```

4. Install the required Python packages:

```bash
pip install -r requirements.txt
```

5. Create a `.env` file and add your Gemini API key:

```text
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

6. Run the application:

```bash
python main.py
```

7. Select your provider:
   - gemini
   - ollama

8. Enter your question to receive an AI-generated response.

## Testing

Run the unit test using:

```bash
python -m unittest test_client.py
```

## Expected Result

The application generates responses using the selected AI provider. The unit test verifies the common LLM client functionality.

## Author
Week 2 Practical Project
