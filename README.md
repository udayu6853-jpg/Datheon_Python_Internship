# Datheon Python Programming Internship

This repository contains the Python projects completed as part of my Datheon Python Programming Internship. These projects helped me practice Python programming, file handling, CSV operations, data processing, automation, regular expressions, and object-oriented programming (OOP).

## 📌 Projects

### Task 1: Hangman Game

A console-based word-guessing game in which the player guesses a hidden word one letter at a time.

**Features**
- Random word selection from `words.txt`
- Limited incorrect guesses
- Displays the current word progress
- Tracks guessed letters
- ASCII hangman display

**Files:** `hangman.py`, `words.txt`

### Task 2: Stock Portfolio Performance Tracker

A Python application that tracks stock investments and calculates portfolio performance using stock price data.

**Features**
- Accepts stock tickers, purchase prices, and quantities
- Retrieves available stock price data using `yfinance`
- Calculates investment value, current value, profit or loss, and percentage return
- Reads stock data from CSV files
- Exports portfolio results to `portfolio_summary.csv`

**Files:** `portfolio.py`, `constituents.csv`, `portfolio_summary.csv`

### Task 3: Automated File Organizer

A Python utility that organizes files into folders based on their extensions.

**Features**
- Uses `os.scandir()` to scan files
- Uses `shutil.move()` to move files
- Categorizes files into Documents, Images, Videos, Archives, and Code
- Handles duplicate filenames by generating alternative names
- Handles permission and file-operation errors
- Supports preview mode before moving files

**File:** `organizer.py`

### Task 4: Rule-Based Interactive Terminal Chatbot

A Python terminal chatbot that uses regular expressions and a JSON FAQ dataset to answer common internship-related questions.

**Features**
- Recognizes greetings such as hello, hi, and hey
- Answers FAQ questions about business hours, project submission, and certificates
- Supports multiple intents in a single message
- Provides fallback responses for unrecognized questions
- Exits gracefully using bye, exit, or quit
- Handles missing or invalid JSON data with error messages

**Files:** `chatbot.py`, `faq.json`

### Task 5: Enterprise Smart Inventory & Asset System

A modular, object-oriented Python application that manages library items, including books, magazines, and digital media.

**Features**
- Uses an abstract base class, `LibraryItem`, with Python's `abc` module
- Implements inheritance through `Book`, `Magazine`, and `DigitalMedia`
- Uses encapsulation with private attributes and property decorators
- Implements polymorphism through item-specific fee calculations and metadata display
- Uses dunder methods such as `__str__`, `__len__`, `__repr__`, and `__eq__`
- Records checkout dates and manages item checkout and return operations
- Displays inventory details and item availability
- Calculates return fees based on the number of days entered
- Maintains an audit report of inventory actions

**Files:** `models.py`, `inventory.py`

## 🛠️ Technologies Used

- Python 3
- Object-oriented programming (OOP)
- Abstract base classes (`abc`)
- Properties and encapsulation
- CSV and JSON file handling
- Regular expressions (`re`)
- File and directory operations (`os`, `pathlib`, `shutil`)
- Random word selection (`random`)
- Stock market data (`yfinance`)
- Date and time handling (`datetime`)
- Exception handling
- Git and GitHub

## ⚙️ Installation and Setup

1. Install Python 3 from the official Python website.
2. Clone this repository:

   ```bash
   git clone https://github.com/udayu6853-jpg/Datheon_Python_Internship.git
   ```

3. Navigate to the project directory:

   ```bash
   cd Datheon_Python_Internship
   ```

4. Install the dependency required for the stock tracker:

   ```bash
   python -m pip install yfinance
   ```

## ▶️ How to Run the Projects

Run each program separately from the project directory.

### Task 1 — Hangman Game

```bash
python hangman.py
```

### Task 2 — Stock Portfolio Tracker

```bash
python portfolio.py
```

### Task 3 — Automated File Organizer

```bash
python organizer.py
```

Before running the organizer, check the target folder and preview setting in `organizer.py`. Keep preview mode enabled until you have verified which files will be organized.

### Task 4 — Terminal Chatbot

```bash
python chatbot.py
```

The chatbot uses `faq.json`, which should remain in the same directory as `chatbot.py`.

### Task 5 — Smart Inventory System

```bash
python inventory.py
```

The inventory application imports its classes from `models.py`. Keep both Python files in the same directory.

## 📚 Learning Outcomes

Through these projects, I practiced:

- Python fundamentals and control flow
- Functions, modules, and exception handling
- Working with CSV and JSON files
- Regular expressions and keyword matching
- Using external Python libraries and stock market data
- File and directory operations
- Automating repetitive tasks
- Object-oriented programming: abstraction, inheritance, encapsulation, and polymorphism
- Implementing properties and special methods
- Testing and debugging Python applications
- Managing projects with Git and GitHub

## 👨‍💻 Author

**Uday**

GitHub: [udayu6853-jpg](https://github.com/udayu6853-jpg)

Developed as part of the Datheon Python Programming Internship.
