# Text Analysis in Python

A Python project that performs text analysis using object-oriented programming. The project defines a `TextAnalyzer` class capable of processing any input string and computing word frequency statistics.

## 📌 Project Overview

This project demonstrates how to analyze text data in Python by:
- Cleaning and formatting raw text (lowercasing and removing punctuation)
- Counting the frequency of every unique word in the text
- Looking up the frequency of a specific word

## 🚀 Features

- **Text Preprocessing**: Converts text to lowercase and strips all punctuation using Python's `string` module.
- **Word Frequency Map**: Generates a dictionary mapping each unique word to its occurrence count.
- **Specific Word Lookup**: Returns the frequency of any given word; returns `0` if the word is not found.

## 🗂️ Project Structure

```
Text-Analysis-in-Python/
│
├── TextAnalysis.py   # Main script containing the TextAnalyzer class
└── README.md         # Project documentation
```

## 🧑‍💻 How It Works

1. A sample string (`givenstring`) is passed to the `TextAnalyzer` class.
2. The constructor cleans the text — lowercases it and removes punctuation — storing it as `fmtText`.
3. `freqAll()` splits the cleaned text into words and builds a frequency dictionary.
4. `freqOf(word)` uses the frequency dictionary to return how many times a specific word appears.

## 📖 Example Usage

```python
from TextAnalysis import TextAnalyzer

text = "Lorem ipsum dolor! diam amet, consetetur Lorem magna."
analyzed = TextAnalyzer(text)

# Print formatted text
print("Formatted Text:", analyzed.fmtText)

# Get frequency of all words
print("Word Frequencies:", analyzed.freqAll())

# Get frequency of a specific word
print("Frequency of 'lorem':", analyzed.freqOf("lorem"))
```

### Sample Output

```
Formatted Text: lorem ipsum dolor diam amet consetetur lorem magna

Word Frequencies: {'lorem': 2, 'ipsum': 1, 'dolor': 1, 'diam': 1, 'amet': 1, 'consetetur': 1, 'magna': 1}

Frequency of 'lorem': 2
```

## 🛠️ Requirements

- Python 3.x
- No external libraries required (uses built-in `string` module only)

## ▶️ Running the Script

```bash
python TextAnalysis.py
```

## 📄 License

This project is open source and available for educational purposes.
