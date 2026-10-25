Datheon Python Programming Internship
This repository contains the Python projects completed as part of my Datheon Python Programming Internship. These projects helped me practice Python programming, file handling, CSV operations, data processing, and automation.
📌 Projects
Task 1: Hangman Game
A console-based word-guessing game in which the player guesses a hidden word one letter at a time.

Features
- Random word selection from words.txt
- Limited incorrect guesses
- Displays the current word progress
- Tracks guessed letters
- ASCII hangman display
Files: hangman.py, words.txt
Task 2: Stock Portfolio Performance Tracker
A Python application that tracks stock investments and calculates portfolio performance using stock price data.

Features
- Accepts stock tickers, purchase prices, and quantities
- Retrieves available stock price data using yfinance
- Calculates investment value, current value, profit or loss, and percentage return
- Reads stock data from CSV files
- Exports portfolio results to portfolio_summary.csv
Files: portfolio.py, constituents.csv, portfolio_summary.csv
Task 3: Automated File Organizer
A Python utility that organizes files into folders based on their extensions.

Features
- Uses os.scandir() to scan files
- Uses shutil.move() to move files
- Categorizes files into Documents, Images, Videos, Archives, and Code
- Handles duplicate filenames by generating alternative names
- Handles permission and file-operation errors
- Supports preview mode before moving files
File: organizer.py
Task 4: Rule-Based Interactive Terminal Chatbot
A Python terminal chatbot that uses regular expressions and a JSON FAQ dataset to answer common internship-related questions.

Features
- Recognizes greetings such as hello, hi, and hey
- Answers FAQ questions about business hours, project submission, and certificates
- Supports multiple intents in a single message
- Provides fallback responses for unrecognized questions
- Exits gracefully using bye, exit, or quit
- Handles missing or invalid JSON data with error messages
Files: chatbot.py, faq.json
🛠️ Technologies Used
- Python 3
- CSV and JSON file handling
- Regular expressions (re)
- os and pathlib
- shutil
- random
- yfinance
- Exception handling
⚙️ Installation and Setup
1. Install Python 3 from the official Python website.
2. Clone this repository:
   git clone https://github.com/udayu6853-jpg/Datheon_Python_Internship.git
3. Navigate to the project directory:
   cd Datheon_Python_Internship
4. Install the dependency required for the stock tracker:
   python -m pip install yfinance
▶️ How to Run the Projects
Run each program separately from the project directory.

Task 1 — Hangman
python hangman.py
Task 2 — Stock Portfolio Tracker
python portfolio.py
Task 3 — File Organizer
python organizer.py
Before running the organizer, check the target folder and preview setting in organizer.py. Keep preview mode enabled until you have verified which files will be organized.

Task 4 — Chatbot
python chatbot.py
The chatbot uses faq.json, which should remain in the same directory as chatbot.py.
📚 Learning Outcomes
Through these projects, I practiced:
- Python fundamentals and control flow
- Functions, modules, and exception handling
- Working with CSV and JSON files
- Regular expressions and keyword matching
- Using external Python libraries and stock market data
- File and directory operations
- Automating repetitive tasks
- Testing and debugging Python applications
- Managing projects with Git and GitHub
👨‍💻 Author
Uday

GitHub: udayu6853-jpg
Developed as part of the Datheon Python Programming Internship.
