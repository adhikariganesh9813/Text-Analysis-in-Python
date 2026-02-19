# Text Analysis in Python

A simple Python script for basic word-frequency analysis on a sample text.

## File
- `TextAnalysis.py`

## What the script does
The script defines a `TextAnalyzer` class and runs it on a predefined sample string.

### 1) Text preprocessing
Inside `__init__`, the input text is normalized by:
- Converting all text to lowercase.
- Removing punctuation using:
  - `text = text.translate(str.maketrans("", "", string.punctuation))`
  - This uses a translation table and removes all standard punctuation characters.

The cleaned result is stored in:
- `self.fmtText`

### 2) Frequency of all unique words
`freqAll()`:
- Splits the formatted text into words.
- Builds a dictionary where each key is a unique word and each value is its count.
- Returns that dictionary.

### 3) Frequency of one word
`freqOf(word)`:
- Calls `freqAll()` to build the dictionary.
- Returns the count if the word exists.
- Returns `0` if not found.

In the current script, the searched word is:
- `lorem`

## How to run
```bash
python3 TextAnalysis.py
```

## Current output behavior
When executed, the script prints:
- The formatted (cleaned) text.
- Frequency map of all unique words.
- Frequency of the selected search word.

## Notes
- The search in `freqOf(word)` is case-sensitive with respect to the already-lowercased dictionary keys. Passing lowercase words (like `"lorem"`) works as expected.
- The frequency logic is correct for this learning/demo script and is easy to read.
