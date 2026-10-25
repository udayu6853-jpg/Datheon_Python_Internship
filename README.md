# Datheon Python Internship

Python programming projects completed as part of the Datheon Python Programming Internship.

## Task 1: Hangman Word Guessing Game

A console-based word guessing game built with Python.

### Features
- Randomly selects a word from `words.txt`.
- Allows letter-by-letter guessing.
- Displays ASCII hangman stages.
- Limits incorrect guesses to six attempts.
- Tracks previously guessed letters.
- Prevents duplicate guesses from reducing attempts.
- Displays victory and defeat messages.

### Files
- `hangman.py` — Hangman game source code.
- `words.txt` — Word list used by the game.

### Run Task 1
```bash
python hangman.py
```

## Task 2: Stock Portfolio Performance Tracker

A Python console application that calculates portfolio investment value and profit or loss using stock market data.

### Features
- Validates ticker symbols using `constituents.csv`.
- Accepts purchase prices and share quantities.
- Retrieves the latest available daily closing price through `yfinance`.
- Calculates invested amount, current estimated value, profit/loss, and percentage return.
- Displays a formatted portfolio summary.
- Saves portfolio results to a CSV file.

**Market data note:** Prices may be delayed or unavailable and are not guaranteed to be live trading quotes. The output is for educational purposes, not investment advice.

### Files
- `portfolio.py` — Stock portfolio tracker.
- `constituents.csv` — S&P 500 company symbols.
- `portfolio_summary.csv` — Optional example output from a test run.

### Requirements
- Python 3
- Internet connection for market data
- `yfinance` Python package

### Install the dependency
```bash
python -m pip install yfinance
```

### Run Task 2
Keep `portfolio.py` and `constituents.csv` in the same folder, then run:

```bash
python portfolio.py
```

The program generates or updates `portfolio_summary.csv` when stock data is retrieved successfully.

## Technologies Used
- Python 3
- `random`
- `csv`
- File handling
- `yfinance`

## Learning Outcomes
- Functions and control flow
- Lists, sets, and dictionaries
- Input validation
- File handling with CSV
- Working with external market-data libraries
- Calculating percentage gain and loss
- Building interactive command-line applications

## Internship
These projects were developed as part of my Python programming practice for the Datheon Python Programming Internship.
