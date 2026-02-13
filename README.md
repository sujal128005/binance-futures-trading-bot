# Binance Futures Trading Bot (Testnet)

A modular Python-based CLI tool for placing Market and Limit orders on the Binance Futures USDT-M Testnet. Built as a technical assessment for the Python Developer role.

## 🚀 Features
- **Order Types:** Supports `MARKET` and `LIMIT` orders.
- **Bi-directional:** Full support for `BUY` (Long) and `SELL` (Short).
- **Validation:** Robust input validation for quantities and prices.
- **Logging:** Structured logging of all API requests and responses to `bot.log`.
- **Error Handling:** Graceful management of network timeouts and API errors.

---

## 🛠️ Setup & Installation

### 1. Prerequisites
- Python 3.8+
- A Binance Futures Testnet account ([Create one here](https://testnet.binancefuture.com/))

### 2. Clone and Install
```bash
# Clone the repository
git clone [https://github.com/YOUR_USERNAME/binance_bot.git](https://github.com/YOUR_USERNAME/binance_bot.git)
cd binance_bot

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
