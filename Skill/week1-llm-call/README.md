# Week 1 Lab: First LLM API Call Using OpenAI

## Objective
To create a Python application that connects to a Large Language Model (LLM) using the OpenAI API and generates a response to a user-provided prompt.

## Tools and Technologies Used
- Python 3.14
- Visual Studio Code (VS Code)
- OpenAI API
- OpenAI Python Library
- python-dotenv
- PowerShell
- Git and GitHub

## Procedure

### Step 1: Create the Project Folder
Created a project folder named `week1-llm-call` on the Desktop and opened it in Visual Studio Code.

### Step 2: Check Python Installation
Checked whether Python was installed by executing the following command in the terminal:

```bash
python --version
```

Python 3.14.10 was installed successfully.

### Step 3: Create a Virtual Environment
Created a virtual environment to isolate the Python packages required for this project.

```bash
python -m venv .venv
```

### Step 4: Activate the Virtual Environment
Activated the virtual environment using PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If execution was blocked, the following command was used to allow scripts temporarily in the current terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

After activation, the terminal displayed `(.venv)`.

### Step 5: Create requirements.txt
Created a file named `requirements.txt` and added the following dependencies:

```text
openai
python-dotenv
```

Installed the dependencies using:

```bash
python -m pip install -r requirements.txt
```

### Step 6: Create the .env File
Created a `.env` file to store the OpenAI API key securely.

```text
OPENAI_API_KEY=your_api_key
```

The API key should not be shared publicly or uploaded to GitHub.

### Step 7: Create the .gitignore File
Created a `.gitignore` file to prevent sensitive files and unnecessary folders from being uploaded to GitHub.

```text
.env
.venv/
__pycache__/
.pytest_cache/
```

### Step 8: Create main.py
Created the Python file `main.py` and wrote the following code:

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY was not found. Check that .env exists "
        "and contains OPENAI_API_KEY=your_key."
    )

client = OpenAI(api_key=api_key)

response = client.responses.create(
    model="g
