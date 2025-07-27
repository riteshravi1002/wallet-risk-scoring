# Wallet Risk Scoring

A Python-based data pipeline that fetches, analyzes, and scores Ethereum wallets interacting with the Compound protocol based on their financial activity.

---

## 📚 Table of Contents

* [Overview](#overview)
* [Features](#features)
* [Project Structure](#project-structure)
* [Installation](#installation)
* [Configuration](#configuration)
* [Usage](#usage)
* [Output](#output)
* [Logging](#logging)
* [Dependencies](#dependencies)
* [License](#license)

---

## 📄 Overview

This tool automates the risk assessment of Ethereum wallets by:

* Fetching wallet addresses from a CSV URL (e.g., Google Sheets)
* Querying the Compound GraphQL API for wallet financial metrics
* Computing feature metrics such as collateral ratios
* Generating normalized scores to assess risk
* Exporting results to CSV with a summary report

---

## ✨ Features

* Integration with Compound's GraphQL API
* CSV wallet ingestion from a public Google Sheet
* Feature engineering (e.g., supply/borrow ratios)
* Custom risk scoring logic
* Exportable reports
* Clean logging and error handling

---

## 📁 Project Structure

```
wallet-risk-scoring/
├── data/
│   └── wallet_scores.csv            # Output file
├── src/
│   ├── main.py                      # Entry point
│   ├── config.py                    # Configuration constants
│   ├── fetch_wallets.py            # Pull wallet list from CSV
│   ├── compound_api.py             # Query Compound Graph API
│   ├── feature_engineering.py      # Feature calculation logic
│   └── scoring.py                  # Wallet scoring logic
└── README.md                       # This file
```

---

## ⚙️ Installation

```bash
# Clone the repo
$ git clone https://github.com/yourusername/wallet-risk-scoring.git
$ cd wallet-risk-scoring

# (Optional) Create virtual environment
$ python -m venv venv
$ source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
$ pip install -r requirements.txt
```

---

## ⚖️ Configuration

Edit `src/config.py`:

```python
WALLETS_CSV_URL = "https://docs.google.com/spreadsheets/...&output=csv"
COMPOUND_GRAPH_URL = "https://api.thegraph.com/subgraphs/name/graphprotocol/compound-v2"
```

---

## 🔄 Usage

Run the pipeline:

```bash
python src/main.py
```

Output:

```
✅ Data collection complete. 103 wallets processed.
✅ Scoring complete.
📦 Output saved to: data/wallet_scores.csv
📊 Summary:
 - Wallets: 103
 - Score range: 300 to 900
 - Average score: 642.12
```

---

## 📊 Output

The resulting CSV (`data/wallet_scores.csv`) includes:

```csv
wallet_id,supply,borrow,health,liquidations,asset_count,collateral_ratio,score
0x123...,1234.0,345.0,2.1,0,3,3.57,680
...
```

---

## 🔧 Logging

Logs are printed to console with levels (INFO, WARNING, ERROR):

```
2025-07-27 22:09:23 [INFO] ✅ Scoring complete.
2025-07-27 22:09:23 [INFO] 📦 Output saved to: data/wallet_scores.csv
```

---

## 📊 Dependencies

* `pandas`
* `requests`
* `logging`

Install them via:

```bash
pip install -r requirements.txt
```

---

## 📃 License

MIT License. See `LICENSE` file for details.

---

## 🚀 Contribution

PRs and suggestions welcome. Please fork the repo and submit pull requests.

---
