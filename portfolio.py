
import csv
from datetime import datetime

import yfinance as yf

DATA_FILE = "constituents.csv"
OUTPUT_FILE = "portfolio_summary.csv"


def load_tickers():
    tickers = set()

    try:
        with open(DATA_FILE, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            for row in reader:
                symbol = row.get("Symbol")
                if symbol:
                    tickers.add(symbol.strip().upper())

    except FileNotFoundError:
        print(f"Error: {DATA_FILE} was not found.")
        return None

    return tickers if tickers else None


def get_positive_number(message):
    while True:
        try:
            value = float(input(message))
            if value > 0:
                return value
            print("Enter a number greater than zero.")
        except ValueError:
            print("Enter a valid number.")


def get_current_price(ticker):
    """Get the latest available price from recent market history."""
    try:
        history = yf.Ticker(ticker).history(period="5d", interval="1d")

        if history.empty:
            return None

        close_prices = history["Close"].dropna()

        if close_prices.empty:
            return None

        return float(close_prices.iloc[-1])

    except Exception as error:
        print(f"Could not fetch market data for {ticker}: {error}")
        return None


def save_results(portfolio):
    fields = [
        "Date", "Ticker", "Buy Price", "Market Price",
        "Quantity", "Invested Amount", "Current Value",
        "Profit/Loss", "Gain/Loss (%)"
    ]

    try:
        with open(OUTPUT_FILE, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fields)

            if file.tell() == 0:
                writer.writeheader()

            writer.writerows(portfolio)

        print(f"\nResults saved to {OUTPUT_FILE}")

    except OSError as error:
        print(f"Could not save CSV file: {error}")


def main():
    valid_tickers = load_tickers()

    if not valid_tickers:
        print("Could not load company symbols. Check constituents.csv.")
        return

    print("=" * 78)
    print("             STOCK PORTFOLIO PERFORMANCE TRACKER")
    print("=" * 78)
    print(f"Loaded {len(valid_tickers)} company symbols.")
    print("Market prices are the latest available daily closing prices.")
    print("They may be delayed and are not guaranteed to be live quotes.\n")

    try:
        count = int(input("How many stocks do you want to track? "))
        if count <= 0:
            print("Enter at least one stock.")
            return
    except ValueError:
        print("Enter a valid whole number.")
        return

    portfolio = []

    for i in range(count):
        print(f"\nStock {i + 1}")

        while True:
            ticker = input("Enter ticker symbol (e.g. AAPL): ").strip().upper()

            if ticker in valid_tickers:
                break

            print("Ticker not found in constituents.csv. Try again.")

        buy_price = get_positive_number("Purchase price per share ($): ")
        quantity = get_positive_number("Number of shares: ")

        print(f"Fetching market data for {ticker}...")
        market_price = get_current_price(ticker)

        if market_price is None:
            print("No market price available. This stock will be skipped.")
            continue

        invested = buy_price * quantity
        current_value = market_price * quantity
        profit_loss = current_value - invested
        percentage = (profit_loss / invested) * 100

        portfolio.append({
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Ticker": ticker,
            "Buy Price": round(buy_price, 2),
            "Market Price": round(market_price, 2),
            "Quantity": quantity,
            "Invested Amount": round(invested, 2),
            "Current Value": round(current_value, 2),
            "Profit/Loss": round(profit_loss, 2),
            "Gain/Loss (%)": round(percentage, 2)
        })

    if not portfolio:
        print("\nNo stock prices could be retrieved. No results saved.")
        return

    total_invested = sum(row["Invested Amount"] for row in portfolio)
    total_value = sum(row["Current Value"] for row in portfolio)
    total_profit_loss = total_value - total_invested
    total_percentage = total_profit_loss / total_invested * 100

    print("\n" + "=" * 112)
    print("PORTFOLIO SUMMARY")
    print("=" * 112)

    headers = (
        f"{'Ticker':<10} {'Buy Price':>12} {'Market Price':>14} "
        f"{'Shares':>10} {'Invested':>14} {'Value':>14} "
        f"{'Profit/Loss':>14} {'Return':>10}"
    )
    print(headers)
    print("-" * 112)

    for row in portfolio:
        print(
            f"{row['Ticker']:<10} "
            f"${row['Buy Price']:>10,.2f} "
            f"${row['Market Price']:>12,.2f} "
            f"{row['Quantity']:>10,.2f} "
            f"${row['Invested Amount']:>12,.2f} "
            f"${row['Current Value']:>12,.2f} "
            f"${row['Profit/Loss']:>12,.2f} "
            f"{row['Gain/Loss (%)']:>8.2f}%"
        )

    print("-" * 112)
    print(f"Total invested : ${total_invested:,.2f}")
    print(f"Current value  : ${total_value:,.2f}")
    print(f"Total P/L      : ${total_profit_loss:,.2f}")
    print(f"Overall return : {total_percentage:.2f}%")

    save_results(portfolio)


if __name__ == "__main__":
    main()
