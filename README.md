# Auto Gmail Creator ✨ (Simulation Tool)

⚠️ Disclaimer: This project is a simulation tool for educational and testing purposes only. It does **not** create real Gmail accounts or interact with Google services, and it does **not** bypass any real security measures like phone/SMS verification.

This repository contains a Python CLI and library for generating mock Gmail account data. It is perfect for developers and testers who need bulk fake account data for unit tests, database seeding, or demonstration purposes.

## Features

- **Simulate bulk account creation**: generate any number of mock accounts with realistic names, email addresses, and secure passwords.
- **Realistic fake data**: uses [Faker](https://faker.readthedocs.io) to create believable names and account details.
- **Offline & safe**: the tool operates completely offline with zero contact to Google.
- **Demo phone verification toggle**: optional flag to mark accounts as phone verified in the output (for demonstration only).
- **Rich CLI experience**: command-line interface powered by Click and Rich for a polished user experience.
- **Export options**: save generated data to JSON or CSV files.
- **Reproducibility**: optional seed for deterministic name generation.

## Installation

You need Python 3.10+ and [Poetry](https://python-poetry.org/).

Clone the repository and install dependencies:

```bash
git clone https://github.com/<your-username>/auto-gmail-creator.git
cd auto-gmail-creator
poetry install
```

Activate the virtual environment:

```bash
poetry shell
```

## Usage

Run the CLI with the `agc` command (installed via Poetry).

Generate 5 accounts (default):

```bash
agc generate
```

Generate 20 accounts with longer passwords:

```bash
agc generate --count 20 --password-length 16
```

Mark accounts as phone verified (demo only):

```bash
agc generate --count 10 --bypass-verification --acknowledge-simulation
```

Export accounts to JSON:

```bash
agc generate --count 50 --output json --output-path my_accounts.json --acknowledge-simulation
```

Set a seed for reproducible names:

```bash
agc generate --count 10 --seed 123 --acknowledge-simulation
```

Please see the CLI help for all options:

```bash
agc generate --help
```

## Development & Testing

Run the test suite:

```bash
poetry run pytest
```

Check code style:

```bash
poetry run ruff check .
poetry run mypy .
```

## Donations

If you find this tool useful and wish to support its development, please consider donating to the following crypto address:

- **ETH / ERC20**: INSERT_YOUR_CRYPTO_WALLET_ADDRESS_HERE

Thank you for your support!

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
