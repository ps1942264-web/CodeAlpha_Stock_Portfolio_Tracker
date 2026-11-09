"""
Task 3: Stock Portfolio Tracker
-------------------------------
A simple console program that calculates the total value of your investment.

  * Stock prices are hardcoded in a dictionary (no internet / API needed).
  * The user enters stock names and quantities.
  * The program shows each holding and the total investment value.
  * The result can optionally be saved to a .txt or .csv file.

Concepts used: dictionary, input/output, basic arithmetic, file handling.
"""

import csv

# Hardcoded stock prices (in US dollars per share)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130,
}


def show_available_stocks():
    """Print the list of stocks the user can choose from."""
    print("Available stocks and prices:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<6} ${price:,.2f}")


def get_quantity(symbol):
    """Keep asking until the user enters a valid whole number (> 0)."""
    while True:
        text = input(f"Enter quantity of {symbol}: ").strip()
        if text.isdigit() and int(text) > 0:
            return int(text)
        print("⚠️  Please enter a whole number greater than 0.")


def collect_portfolio():
    """Ask the user for stocks and quantities. Returns {symbol: quantity}."""
    portfolio = {}

    while True:
        symbol = input("\nEnter stock symbol (or type 'done' to finish): ").strip().upper()

        if symbol == "DONE":
            break
        elif symbol not in STOCK_PRICES:
            print(f"⚠️  '{symbol}' is not in the price list. Please choose from the list above.")
        else:
            quantity = get_quantity(symbol)
            # If the stock was already entered, add to the existing quantity
            portfolio[symbol] = portfolio.get(symbol, 0) + quantity
            print(f"✅ Added {quantity} share(s) of {symbol}.")

    return portfolio


def calculate_total(portfolio):
    """Total investment = sum of (price x quantity) for every stock."""
    total = 0
    for symbol, quantity in portfolio.items():
        total += STOCK_PRICES[symbol] * quantity
    return total


def display_summary(portfolio, total):
    """Print a neat table of the portfolio and the total value."""
    print("\n" + "=" * 42)
    print("          PORTFOLIO SUMMARY")
    print("=" * 42)
    print(f"{'Stock':<8}{'Price':>10}{'Qty':>8}{'Value':>14}")
    print("-" * 42)
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        print(f"{symbol:<8}{price:>10,.2f}{quantity:>8}{value:>14,.2f}")
    print("-" * 42)
    print(f"{'TOTAL INVESTMENT:':<28}${total:>13,.2f}")
    print("=" * 42)


def save_to_txt(portfolio, total, filename="portfolio_summary.txt"):
    """Save the summary as a plain text file."""
    with open(filename, "w") as file:
        file.write("PORTFOLIO SUMMARY\n")
        file.write("-----------------\n")
        for symbol, quantity in portfolio.items():
            price = STOCK_PRICES[symbol]
            file.write(f"{symbol}: {quantity} x ${price:,.2f} = ${price * quantity:,.2f}\n")
        file.write("-----------------\n")
        file.write(f"Total investment: ${total:,.2f}\n")
    print(f"💾 Saved to {filename}")


def save_to_csv(portfolio, total, filename="portfolio_summary.csv"):
    """Save the summary as a CSV file (opens in Excel)."""
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Price", "Quantity", "Value"])
        for symbol, quantity in portfolio.items():
            price = STOCK_PRICES[symbol]
            writer.writerow([symbol, price, quantity, price * quantity])
        writer.writerow(["TOTAL", "", "", total])
    print(f"💾 Saved to {filename}")


def main():
    print("==============================")
    print("   STOCK PORTFOLIO TRACKER")
    print("==============================")
    show_available_stocks()

    portfolio = collect_portfolio()

    if not portfolio:
        print("\nNo stocks were entered. Goodbye!")
        return

    total = calculate_total(portfolio)
    display_summary(portfolio, total)

    # Optional: save the result to a file
    choice = input("\nSave result to a file? (txt / csv / no): ").strip().lower()
    if choice == "txt":
        save_to_txt(portfolio, total)
    elif choice == "csv":
        save_to_csv(portfolio, total)
    else:
        print("Result not saved.")

    print("\nThanks for using the Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()
