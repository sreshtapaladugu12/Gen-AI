 Week 3 – LLM Monitoring with MongoDB

 1. Project Overview

The objective of this project is to monitor Large Language Model (LLM) API usage by tracking token consumption, response time, and estimated cost.

The project supports two LLM providers:

- **Gemini** – Cloud-based LLM provided by Google.
- **Ollama** – Runs an LLM locally on the computer.

The usage details of each request are stored in MongoDB for monitoring and analysis.

 2. Objectives

- Connect to different LLM providers using a common client.
- Track input and output token usage.
- Calculate total tokens used.
- Measure response latency.
- Estimate API usage cost.
- Store usage records in MongoDB.
- Handle errors using timeouts and retry mechanisms.
- Test the LLM client using unit tests.

 3. Technologies and Tools Used

| Technology / Tool | Purpose |
|---|---|
| Python | Main programming language |
| Visual Studio Code | Code editor |
| Gemini API | Connect to Google's Gemini model |
| Ollama | Run an LLM locally |
| MongoDB Atlas | Store API usage records |
| PyMongo | Connect Python to MongoDB |
| Google GenAI SDK | Communicate with Gemini |
| Requests | Communicate with Ollama |
| python-dotenv | Load environment variables from `.env` |
| unittest | Test the application |
| Git and GitHub | Version control and project submission |
| PowerShell | Run commands and execute Python files |

 4. Project Structure

```text
Week3/
│
├── main.py
├── llm_client.py
├── usage_logger.py
├── test_client.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
└── screenshots/
    ├── 01_test_output.png
    ├── 02_gemini_output.png
    └── 03_mongodb_output.png
```

**Note:** The `.env` file contains private credentials and must not be uploaded to GitHub.

## 5. Procedure Followed

### Step 1: Project Setup

- Created a Week3 project folder in VS Code.
- Created a Python virtual environment.
- Activated the virtual environment.
- Created the required Python files.
- Installed the required Python libraries.

 Step 2: Environment Configuration

- Created a `.env` file.
- Added the Gemini API key.
- Added the MongoDB connection URI.
- Configured the input and output token pricing values used for estimated cost calculation.
- Created a `.gitignore` file to exclude `.env`, `venv/`, and Python cache files.

 Step 3: MongoDB Atlas Setup

- Created or accessed a MongoDB Atlas cluster.
- Configured database access and network access.
- Connected the Python application to MongoDB.
- Created the database `llm_monitoring`.
- Created the collection `api_usage`.

Step 4: Implemented Usage Logger

Created `usage_logger.py` to:

- Connect Python to MongoDB.
- Check whether the database connection is working.
- Store usage records in the `api_usage` collection.
- Record timestamps, token usage, response latency, estimated cost, and request status.
- Retry database writes when a temporary error occurs.

 Step 5: Implemented LLM Client

Created `llm_client.py` to:

- Define a common interface for LLM providers.
- Implement the Gemini provider.
- Implement the Ollama provider.
- Send prompts to the selected provider.
- Capture token usage.
- Measure response latency.
- Calculate estimated API cost.
- Handle errors and retry temporary failures.
- Send usage information to MongoDB.

### Step 6: Implemented Main Application

Created `main.py` to:

1. Load environment variables.
2. Connect to MongoDB.
3. Ask the user to select a provider (`gemini` or `ollama`).
4. Accept a question from the user.
5. Send the question to the selected LLM provider.
6. Display the generated answer.
7. Save usage details in MongoDB.
8. Handle errors and close the database connection.

### Step 7: Implemented Unit Testing

Created `test_client.py` to test the LLM client using a fake provider and fake logger.

The test checks:

- Whether the generated answer is correct.
- Whether usage details are logged.
- Whether total token usage is calculated correctly.
- Whether the request status is recorded as successful.

### Step 8: Installed Dependencies

Installed all required Python packages using:

```powershell
pip install -r requirements.txt
```

### Step 9: Tested the Application

Ran the unit test:

```powershell
python -m unittest test_client.py
```

Ran the main application:

```powershell
python main.py
```

Selected Gemini or Ollama and entered a question to generate a response.

### Step 10: Verified MongoDB Records

Opened MongoDB Atlas and checked:

- Database: `llm_monitoring`
- Collection: `api_usage`

Verified that usage records were being saved.

### Step 11: GitHub Submission

- Added the Week3 project folder inside the `SKILL` folder of the Gen-AI GitHub repository.
- Used Git to stage and commit the project files.
- Prepared the project for pushing to GitHub.
- Kept private credentials and the virtual environment excluded using `.gitignore`.

## 6. Monitoring Information Recorded

The application tracks the following information:

| Field | Description |
|---|---|
| Timestamp | Date and time of the request |
| Provider | Gemini or Ollama |
| Model | Model used for generating the answer |
| Prompt | User's input question |
| Input Tokens | Tokens used in the input |
| Output Tokens | Tokens generated in
