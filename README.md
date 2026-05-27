# Personal Finance Analyzer

A Python project that reads your bank transactions from a CSV file and generates a visual finance dashboard with charts and spending insights.

# What it does

- Reads your bank transactions from a CSV file
- Automatically categorizes every transaction into Food, Groceries, Transport, Bills, Health, Shopping, Entertainment and Income
- Calculates your total income, total expenses, savings and savings rate
- Generates 3 charts as image files
- Produces a clean HTML dashboard that opens in your browser showing everything in one place


## Project Structure

personal-finance-analyzer/
├── analyzer/
│   ├── loader.py
│   ├── categorizer.py
│   ├── analysis.py
│   └── visualizer.py
├── data/
│   └── transactions.csv
├── templates/
│   └── dashboard.html
├── config.py
├── main.py
└── requirements.txt


# Requirements

- Python 3.8 or above


# How to Run

*Step 1 — Clone the repository*

*Step 2 — Create virtual environment*

python -m venv .venv

*Step 3 — Activate virtual environment*

.venv\Scripts\activate

*Step 4 — Install required libraries*

pip install -r requirements.txt

*Step 5 — Run the project*

python main.py

*Step 6 — View your dashboard*

After running, open `output/dashboard.html` in your browser.


# CSV Format

Your CSV file must have exactly these three columns:

| Column | Format | Example |
|---|---|---|
| Date | YYYY-MM-DD | 2024-01-01 |
| Description | Plain text | Swiggy Food Order |
| Amount | Number. Negative for expense, Positive for income | -450 |

Example:
Date,Description,Amount
2024-01-01,Salary Credited,50000
2024-01-02,Swiggy Food Order,-450
2024-01-03,DMart Grocery,-3200

---

## Categories

Transactions are automatically categorized based on keywords defined in config.py.

| Category | Keywords |
|---|---|
| Food | swiggy, zomato |
| Groceries | dmart, bigbasket, zepto |
| Transport | ola, uber, petrol |
| Bills | electricity, internet, mobile recharge |
| Health | medical, doctor, gym |
| Shopping | amazon |
| Income | salary, freelance |
| Entertainment | netflix, spotify, bookmyshow |

You can add your own keywords by editing config.py.

## Built With

- Python 3
- Pandas
- Matplotlib
- Seaborn
- Jinja2


