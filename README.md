# Coin Notifier

Coin Notifier is a simple Python scraper that pulls cryptocurrency data from a private API on [arzplus.net](https://arzplus.net) and sends the data to a predefined Telegram account. This project uses [Poetry](https://python-poetry.org/) for dependency management and packaging.

## Requirements

- Python 3.11 or above
- Telegram bot API key and chat ID for sending notifications
- [Poetry](https://python-poetry.org/) installed on your system

## Setup

```
poetry install
poetry shell
python -m crypto_notifer.notifier
```
