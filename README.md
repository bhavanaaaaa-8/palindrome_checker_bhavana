# Palindrome Checker

## Description
This Python program checks whether a word or sentence is a palindrome. A palindrome is a word or sentence that reads the same forward and backward.

## Features
- Accepts a word or sentence as input.
- Converts all letters to lowercase.
- Removes spaces before checking.
- Uses string slicing to reverse the normalized text.
- Displays a clear result indicating whether the input is a palindrome.

## Concepts Used
- `input()` for user input.
- `lower()` for case normalization.
- `replace()` for removing spaces.
- String slicing (`[::-1]`) for reversing text.
- `if-else` statements for decision-making.

## Example Output

```text
Enter a word or sentence: Never Odd Or Even
It is a palindrome!
```

```text
Enter a word or sentence: Hello World
It is not a palindrome!
```

## How to Run
1. Install Python 3 if it is not already installed.
2. Save the program as `palindrome_checker.py`.
3. Open a terminal in the folder containing the file.
4. Run the command:

```bash
python palindrome_checker.py
```

## Limitations
- Ignores capitalization and spaces only.
- Punctuation and special characters are not removed.
- Empty input will be treated as a palindrome.

## Purpose
This project demonstrates basic Python string manipulation, normalization, slicing, and conditional statements.
