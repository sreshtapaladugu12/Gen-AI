# Week 6 – Generative AI Programming

## Overview

This project performs a baseline evaluation of a Large Language Model (LLM) using a Golden Question Set. The model used for this experiment is **Llama 3.2**, running locally through Ollama.

The project evaluates the model's responses against expected answers using keyword-based scoring. The results are saved in a CSV file for analysis.

**Release Version:** v0.1

## Objectives

- Set up and run Llama 3.2 using Ollama.
- Create a Golden Question Set with questions, expected answers, keywords, and sources.
- Connect Python with the locally running LLM through the Ollama API.
- Generate answers for all questions in the Golden Question Set.
- Evaluate responses using keyword-based scoring.
- Save evaluation results in a CSV file.
- Perform the first baseline evaluation and document Release v0.1.

## Technologies Used

- Python
- Ollama
- Llama 3.2
- JSON
- CSV
- Requests library
- Visual Studio Code

## Project Structure

```text
week6/
│
├── golden_set.json
├── main.py
├── requirements.txt
└── baseline_results.csv
```

### File Description

| File | Description |
|---|---|
| `golden_set.json` | Contains questions, expected answers, keywords, and source URLs. |
| `main.py` | Python program that runs the baseline evaluation. |
| `requirements.txt` | Contains the required Python dependency. |
| `baseline_results.csv` | Automatically generated file containing evaluation results. |

## Procedure

### Step 1: Check Ollama Installation

Check the installed Ollama version using PowerShell:

```powershell
ollama --version
```

### Step 2: Download the Llama 3.2 Model

Download the model using:

```powershell
ollama pull llama3.2
```

The downloaded model is used to generate responses to the questions in the
