# Stock Portfolio Tracker 📈

A simple console program in Python that calculates the total value of your stock investment using manually defined prices.

## Features
- Hardcoded dictionary of stock prices (no internet or API needed)
- Enter stock symbols and quantities one by one
- Repeated entries for the same stock are added together
- Input validation for unknown symbols and invalid quantities
- Neat summary table with the total investment value
- Optionally save the result to a `.txt` or `.csv` file

## Concepts Used
dictionary · input/output · basic arithmetic · file handling

## Available Stocks
| Symbol | Price (USD) |
|---|---|
| AAPL | 180 |
| TSLA | 250 |
| GOOGL | 140 |
| MSFT | 330 |
| AMZN | 130 |

To add or change a stock, edit the `STOCK_PRICES` dictionary at the top of `stock_tracker.py`.

## How to Run
1. Install [Python 3](https://www.python.org/downloads/)
2. Clone this repository or download `stock_tracker.py`
3. Run in a terminal:
   ```bash
   python stock_tracker.py
   ```

## Sample Run
```
Enter stock symbol (or type 'done' to finish): aapl
Enter quantity of AAPL: 10
Enter stock symbol (or type 'done' to finish): tsla
Enter quantity of TSLA: 2
Enter stock symbol (or type 'done' to finish): done

==========================================
          PORTFOLIO SUMMARY
==========================================
Stock        Price     Qty         Value
------------------------------------------
AAPL        180.00      10      1,800.00
TSLA        250.00       2        500.00
------------------------------------------
TOTAL INVESTMENT:           $     2,300.00
==========================================
```
