# Week 5 – Tokenization and Token Economics

## Aim

To understand and compare tokenization approaches used in Natural Language Processing (NLP) and Large Language Models (LLMs), and to calculate API costs, budgets, and context window usage.

The experiment covers:
- English, Telugu, and Hindi token comparison
- BPE (Byte Pair Encoding)
- WordPiece
- SentencePiece
- API cost calculation and budgeting
- Context window calculation

---

## 1. Project Setup

Created a project folder named `week5` and opened it in Visual Studio Code.

Created a Python file named:

`week5.py`

---

## 2. Installing Required Library

The experiment uses the Transformers library.

The following command was executed in the VS Code terminal:

```powershell
pip install transformers
```

The Transformers library is used to load and work with different tokenizer models.

---

## 3. Importing Required Libraries

The following libraries were imported:

```python
from transformers import AutoTokenizer
import csv
```

- `AutoTokenizer` is used to load tokenizer models.
- `csv` is used to save token comparison results into a CSV file.

---

## 4. Part 1 – English, Telugu and Hindi Token Comparison

Three sentences were provided in different languages:

- English: Artificial Intelligence helps students learn new technologies.
- Telugu: కృత్రిమ మేధస్సు విద్యార్థులకు కొత్త సాంకేతికతలను నేర్చుకోవడంలో సహాయపడుతుంది.
- Hindi: कृत्रिम बुद्धिमत्ता छात्रों को नई तकनीक सीखने में मदद करती है।

Three tokenizer models were selected:

| Tokenizer | Model |
|---|---|
| BPE (GPT-2) | openai-community/gpt2 |
| WordPiece (Multilingual BERT) | google-bert/bert-base-multilingual-cased |
| SentencePiece (mT5) | google/mt5-small |

The tokenizer models were loaded using `AutoTokenizer.from_pretrained()`.

Each sentence was processed using all three tokenizers.

The following values were calculated:

- Word Count
- Token Count
- Token Ratio

The token ratio was calculated using:

```python
token_ratio = token_count / word_count
```

The tokens were displayed using:

```python
tokens = tokenizer.convert_ids_to_tokens(token_ids)
```

The token comparison
