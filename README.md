# Datheon Python Programming Internship

This repository contains the Python projects completed as part of my **Datheon Python Programming Internship**. These projects helped me practice Python programming, file handling, CSV operations, data processing, and automation.

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

## 🛠️ Technologies Used

- Python 3
- CSV file handling
- `os` and `pathlib`
- `shutil`
- `random`
- `yfinance`
- Basic exception handling

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

**Task 1 — Hangman**

```bash
python hangman.py
```

**Task 2 — Stock Portfolio Tracker**

```bash
python portfolio.py
```

**Task 3 — File Organizer**

```bash
python organizer.py
```

Before running the organizer, check the target folder and preview setting in `organizer.py`. Keep preview mode enabled until you have verified which files will be organized.

## 📚 Learning Outcomes

Through these projects, I practiced:

- Python fundamentals and control flow
- Functions, modules, and exception handling
- Working with CSV files
- Using external Python libraries and stock market data
- File and directory operations
- Automating repetitive tasks
- Testing and debugging Python applications
- Managing projects with Git and GitHub

## 👨‍💻 Author

**Uday**

GitHub: [udayu6853-jpg](https://github.com/udayu6853-jpg)

---

*Developed as part of the Datheon Python Programming Internship.*
