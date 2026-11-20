# Week 4 – Tokenizer Comparison Lab

## Aim

To understand and compare three popular tokenization approaches used in Natural Language Processing (NLP) and Large Language Models (LLMs):

- Byte Pair Encoding (BPE)
- WordPiece
- SentencePiece

The experiment evaluates how these tokenizers process English, Telugu, and Hindi text and compares their token counts.

---

## 1. Project Setup

Created a project folder named:

`week4-tokenizer-comparison`

The project folder was opened in Visual Studio Code.

---

## 2. Creating requirements.txt

Created a file named `requirements.txt` containing the following required libraries:

```text
transformers
sentencepiece
tiktoken
protobuf
```

These libraries are used for working with different tokenizer implementations.

---

## 3. Installing Required Libraries

The required libraries were installed using the following command in the VS Code terminal:

```bash
pip install -r requirements.txt
```

---

## 4. Creating the Python File

Created a Python file named:

`tokenizer_lab.py`

The file contains the code for the tokenizer comparison experiment.

---

## 5. Importing Required Libraries

The following libraries were imported:

```python
from transformers import AutoTokenizer
import csv
```

- `AutoTokenizer` is used to load tokenizer models.
- `csv` is used to save the experiment results into a CSV file.

---

## 6. Step 1 – Input Sentences in Three Languages

Three sentences were provided in English, Telugu, and Hindi.

```python
sentences = {
    "English": "Artificial Intelligence is transforming education and healthcare.",
    "Telugu": "కృత్రిమ మేధస్సు విద్య మరియు వైద్య రంగాలను మారుస్తోంది.",
    "Hindi": "कृत्रिम बुद्धिमत्ता शिक्षा और स्वास्थ्य सेवा को बदल रही है।"
}
```

These sentences were used to compare how different tokenizers process multiple languages.

---

## 7. Step 2 – Selecting Three Tokenizer Models

Three tokenizer models were selected:

| Tokenizer | Model |
|---|---|
| BPE (GPT-2) | openai-community/gpt2 |
| WordPiece (Multilingual BERT) | google-bert/bert-base-multilingual-cased |
| SentencePiece (mT5 Unigram) | google/mt5-small |

Each tokenizer was configured with the appropriate `use_fast` setting.

---

## 8. Step 3 – Loading the Tokenizers

The tokenizer models were loaded using:

```python
AutoTokenizer.from_pretrained()
```

The loaded tokenizers were stored in a dictionary named `loaded_tokenizers`.

The program displays the loading status of each tokenizer.

---

## 9. Step 4 – Tokenizing the Sentences

Each sentence was processed using all three tokenizer models.

The following operations were performed:

- Converted sentences into token IDs.
- Converted token IDs into readable token pieces.
- Counted the number of tokens.
- Counted the number of whitespace-separated words.
- Calculated the token ratio.

The token ratio was calculated using:

```python
token_ratio = token_count / word_count if word_count else 0
```

The results were displayed for each language and tokenizer.

---

## 10. Step 5 – Displaying the Comparison Table

The program displays a comparison table containing:

| Column | Description |
|---|---|
| Language | Language of the sentence |
| Tokenizer | Tokenizer model used |
| Words | Total word count |
| Tokens | Total token count |
| Ratio | Token ratio |

The comparison table helps evaluate the tokenization results across the three languages and tokenizer models.

---

## 11. Step 6 – Exporting Results to CSV

The experiment results were exported to a CSV file using the Python `csv` module.

The generated file is:

`tokenizer_results.csv`

The CSV file contains the following fields:

- Language
- Tokenizer
- Word_Count
- Token_Count
- Token_Ratio

The results were saved using UTF-8 encoding with BOM.

---

## 12. Execution

The Python program was executed using the following command in the VS Code terminal:

```bash
python tokenizer_lab.py
```

The tokenizer models were loaded, and the sentences were processed to generate the tokenization results and comparison table.

---

## 13. Generated Output File

The experiment generates the following CSV file automatically:

```text
tokenizer_results.csv
```

This file contains the tokenization comparison results for English, Telugu, and Hindi using the three tokenizer models.

---

## 14. Project Structure

```text
week4-tokenizer-comparison/
│
├── requirements.txt
├── tokenizer_lab.py
└── tokenizer_results.csv
```

---

## Conclusion

The experiment compares BPE, WordPiece, and SentencePiece tokenization approaches using English, Telugu, and Hindi sentences.

The token counts and token ratios are calculated and compared to understand how different tokenizers process text in different languages. The results are displayed in the terminal and exported into a CSV file for further analysis.

