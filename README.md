---

```markdown
# Binance Futures Trading Bot (Testnet)

A modular Python CLI application for placing **Market** and **Limit** orders on the **Binance Futures USDT-M Testnet**.  
Built as a technical assessment for a Python Developer role, with focus on clean structure, logging, validation, and error handling.

---

## 📌 Overview

This bot allows users to place futures orders directly from the command line using Binance Futures Testnet APIs.  
It is designed with modular architecture, structured logging, and defensive error handling to simulate production-style trading tools.

---

## 🚀 Features

- ✅ Bi-directional trading (BUY and SELL)
- ✅ Supports MARKET and LIMIT order types
- ✅ CLI interface using `click`
- ✅ Structured logging to console and file
- ✅ Environment-based credential management
- ✅ Input validation and API constraint checks
- ✅ Graceful error handling for network and API failures
- ✅ Testnet-only safe execution

---

## 🧰 Tech Stack

- Python 3.8+
- Binance Futures API (USDT-M Testnet)
- Click (CLI interface)
- python-dotenv (environment config)
- Logging module (structured logs)

---

## 📂 Project Structure

```

binance-futures-trading-bot/
│
├── cli.py                 # CLI entry point
│
├── bot/
│   ├── client.py          # Binance client initialization (testnet)
│   ├── orders.py          # Order execution logic
│   ├── logger.py          # Logging configuration
│
├── requirements.txt
├── .env.example
├── bot.log                # Runtime logs
└── README.md

````

---

## ⚙️ Setup & Installation

### 1️⃣ Prerequisites

- Python 3.8 or higher
- Binance Futures Testnet account
- Testnet API key and secret

---

### 2️⃣ Clone Repository

```bash
git clone https://github.com/sujal128005/binance-futures-trading-bot.git
cd binance-futures-trading-bot
````

---

### 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

---

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuration

Create a `.env` file in the project root.

```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

You can use `.env.example` as a template.

---

## 💻 Usage

All orders are placed through the CLI.

---

### ▶️ Place Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.005
```

---

### ▶️ Place Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.005 --price 98000
```

---

## 🧠 Order Logic & Assumptions

* Minimum notional value on Binance Futures Testnet is assumed to be **100 USDT**
* Orders below minimum notional are rejected and logged
* LIMIT orders use default **GTC (Good Till Cancelled)**
* Symbol input is auto-converted to uppercase
* Bot assumes sufficient margin balance exists

---

## 📝 Logging

All activity is logged to:

```
bot.log
```

Includes:

* API requests
* API responses
* Validation failures
* Network errors
* Order confirmations

Console logs are also enabled for quick debugging.

---

## 🛡️ Validation & Error Handling

The application checks:

* LIMIT orders must include price
* Quantity must be valid numeric value
* API response errors are captured and logged
* Network failures are handled safely
* Invalid symbols or parameters are reported clearly

---

## 🧪 Testnet Safety

This bot is configured **only for Binance Futures Testnet**.
No real funds are used.

---

## 📌 Possible Future Improvements

* Position tracking
* Stop loss / take profit support
* Websocket price streaming
* Strategy plug-in system
* Backtesting module
* Docker support

---

## 👨‍💻 Author

**Sujal**
Python Developer Candidate
Futures Trading Bot — Technical Assessment Project

---

## 📄 License

This project is for assessment and educational purposes.

```

---
```
