# Auto Gmail Creator ✨

> **Disclaimer**  
> This website presents a *simulation tool* for educational and testing purposes. It **does not** create real Gmail accounts, interact with Google’s services, or bypass any security measures. Use responsibly.

## 🌏 Overview

Auto Gmail Creator lets developers, testers, and marketers generate realistic mock Gmail accounts without touching external APIs. It uses the [`faker`](https://faker.readthedocs.io/en/master/) library to create plausible names and emails, builds unique usernames, and generates secure passwords using Python’s `secrets` module. Each account also comes with a recovery email from a rotating set of providers.

The tool is written in Python and packaged as a CLI via `click` with rich terminal output from the `rich` library. It’s type‑checked with `mypy`, linted with `ruff`, and covered by tests using `pytest`.

## 🚀 Features

- **Bulk simulation** — Generate any number of mock Gmail accounts.
- **Unique credentials** — Ensures unique usernames and emails in a single run.
- **Secure passwords** — Random passwords with uppercase, lowercase, digits, and symbols.
- **Recovery email rotation** — Uses various domains for recovery addresses.
- **Demo‑only verification flag** — A `--bypass-verification` option to mark `phone_verified` as `True` in the output (no real verification occurs).
- **Export options** — Save your generated data to CSV or JSON.
- **Reproducibility** — Seedable random generator for reproducible names/usernames.
- **Password length control** — Specify password lengths between 8 and 128 characters.

## 💻 Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/auto-gmail-creator.git
   cd auto-gmail-creator
   ```

2. **Install dependencies**  
   This project uses [Poetry](https://python-poetry.org/) for dependency management.  
   ```bash
   poetry install
   ```

3. **Activate the environment**  
   ```bash
   poetry shell
   ```

## 🛠️ Usage

Run the CLI via the `agc` command:

```bash
# Generate 5 accounts (default)
agc generate

# Generate 20 accounts
agc generate --count 20

# Save 100 accounts to a CSV
agc generate --count 100 --output csv --output-path accounts.csv

# Use a seed for reproducibility and longer passwords
agc generate --count 10 --seed 123 --password-length 16

# Mark phone verification as true in the output (demo only)
agc generate --count 10 --bypass-verification
```

### Helpful options

| Option                  | Description                                                  |
|------------------------ |--------------------------------------------------------------|
| `--count <int>`         | Number of accounts to generate (default: 5)                 |
| `--output json/csv`     | Export format (when specified)                              |
| `--output-path <file>`  | Custom export path                                          |
| `--seed <int>`          | Seed for reproducible names/usernames                       |
| `--password-length`     | Length of generated passwords (8–128, default: 12)          |
| `--bypass-verification` | Toggle `phone_verified` to `True` in the output (demo only) |
| `--acknowledge-simulation` | Explicitly acknowledge that this is a simulation tool     |

## 💻 Development

This project follows modern Python best practices:

- **Static typing** with `mypy`
- **Linting** with `ruff`
- **CI** with GitHub Actions on Python 3.10 and 3.11
- **Tests** using `pytest` and `click.testing`

To run tests and linters:

```bash
poetry run ruff check .
poetry run mypy .
poetry run pytest -q
```

## 💖 Support / Donations

If you find this project useful and want to support development, you can send crypto donations here:

- **Bitcoin (BTC):** your_btc_wallet_id
- **Ethereum (ETH):** your_eth_wallet_id
- **USDT (TRC20):** your_usdt_wallet_id

Thank you for your support!

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Built with ❤️ using Python, Poetry, Click, Faker, and Rich.
