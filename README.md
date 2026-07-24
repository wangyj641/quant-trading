# Quant Trading Platform

A modern Python-based quantitative trading platform for research, backtesting, and automated trading.

The project is designed with clean architecture and focuses on maintainability, extensibility, and production-ready code. It supports historical market data management, technical indicators, trading strategies, backtesting, and future integration with Interactive Brokers (IBKR).

---

## Features

### Market Data

- Historical market data downloader
- Multiple data providers
- SQLite data storage
- Repository pattern
- Incremental data synchronization

### Technical Indicators

- Moving Average (MA)
- Exponential Moving Average (EMA)
- RSI
- MACD
- ATR
- VWAP

### Strategy Engine

- Strategy abstraction
- Moving Average Cross Strategy
- Extensible strategy framework

### Backtesting

- Historical backtesting
- Trade history
- Equity curve
- Maximum drawdown
- Performance report

### Future Roadmap

- Parameter optimization
- Portfolio backtesting
- Position sizing
- Risk management
- Paper Trading
- Interactive Brokers integration
- Live trading
- AI-assisted market analysis

---

# Project Structure

```text
app/
│
├── backtest/
├── config/
├── constants/
├── converters/
├── data/
├── database/
├── domain/
├── indicators/
├── repository/
├── services/
├── strategy/
├── visualization/
└── utils/

tests/

docs/

main.py
```

---

# Architecture

```text
                    +----------------------+
                    |   Data Provider      |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |   Downloader         |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | SQLite Database      |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Repository           |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | MarketBar            |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Indicator Engine     |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Strategy             |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Backtest Engine      |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Performance Report   |
                    +----------------------+
```

---

# Technology Stack

- Python 3.13
- Pandas
- SQLAlchemy
- SQLite
- Matplotlib
- NumPy
- Pytest

Future:

- Interactive Brokers API
- Plotly
- FastAPI
- Docker

---

# Installation

Clone the repository

```bash
git clone https://github.com/wangyj641/quant-trading.git

cd quant-trading
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Usage

Download historical market data

```bash
python main.py download
```

Run strategy

```bash
python main.py strategy
```

Run backtest

```bash
python main.py backtest
```

Run unit tests

```bash
pytest
```

---

# Development Roadmap

## Version 0.1

- [x] Historical data downloader
- [x] SQLite repository
- [x] MarketBar domain model
- [x] Indicator Engine
- [x] MA Indicator
- [x] MA Cross Strategy
- [x] Backtest Engine
- [x] Equity Curve
- [x] Maximum Drawdown

## Version 0.2

- [ ] RSI
- [ ] MACD
- [ ] ATR
- [ ] VWAP
- [ ] Professional charts
- [ ] Transaction costs
- [ ] Slippage

## Version 0.3

- [ ] Portfolio management
- [ ] Position sizing
- [ ] Risk management
- [ ] Grid search optimization

## Version 1.0

- [ ] Interactive Brokers Paper Trading
- [ ] Live Trading
- [ ] AI Market Analysis
- [ ] Web Dashboard

---

# Design Principles

- Clean Architecture
- Domain-Driven Design (DDD)
- Repository Pattern
- SOLID Principles
- Test-Driven Development (TDD)
- Separation of Concerns

---

# Testing

Run all tests

```bash
pytest
```

Generate coverage report

```bash
pytest --cov=app
```

---

# License

MIT License
