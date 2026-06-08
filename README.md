# Footstats CLI

> Football player stats, transfers, and market values — straight from your terminal.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/Marin2409/footstats-cli/blob/main/LICENSE)
![UV](https://img.shields.io/badge/package%20manager-uv-purple?style=flat)
![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg)

---

## Overview

Footstats is an open-source CLI tool that lets you search for any football player and retrieve their profile, transfer history, and match statistics — all from your terminal, powered by data from Transfermarkt.

---

## Features

- **Player Search** — Search any player by name
- **Player Profile** — Market value, age, club, position, nationality, and more
- **Transfer History** — Full transfer history with fees and market values
- **Match Stats** — Per-game stats including goals, assists, cards, minutes, passes, and shots
- **Interactive Menu** — Navigate with a single keypress
- **Direct Commands** — Call any command directly with arguments

---

## Data Sources

| Source | Data |
|--------|------|
| [Transfermarkt](https://www.transfermarkt.com/) | Market value, transfers, match stats, player profile |

---

## Requirements

- [Python 3.13+](https://www.python.org/downloads/)

---

## Installation

**With pip**

```bash
pip install footstats-cli
```

**With uv (recommended)**

```bash
uv tool install footstats-cli
```

That's it — the `footstats` command is now available globally in your terminal.

## Upgrade to latest version
```bash
# pip
pip install footstats-cli --upgrade

# uv
uv tool upgrade footstats-cli
```

## Uninstall
```bash
# pip
pip uninstall footstats-cli

# uv
uv tool uninstall footstats-cli
```

---

## Usage

**Interactive menu**

```bash
footstats
```

**Direct commands**

```bash
footstats player "Cristiano Ronaldo"
footstats transfer-history "Lionel Messi"
footstats stats "Erling Haaland"
```

**Options**

```bash
footstats --help
footstats --version
```

---

## Configuration

By default the tool works out of the box. To customize request behavior, create a `.env` file in your working directory:

```dotenv
USER_AGENT=Mozilla/5.0 (Windows NT 10.0; Win64; x64)...
ACCEPT_LANGUAGE=en-US,en;q=0.5
ACCEPT_ENCODING=gzip, deflate
REQUEST_DELAY=3.0   # seconds between requests — increase if getting blocked
```

---

## Project Structure

```
footstats-scraper/
├── src/
│   ├── cli/
│   │   ├── main.py          # CLI entry point
│   │   └── utils/           # Display helpers
│   ├── models/              # Dataclasses
│   ├── providers/           # Scraping logic
│   └── utils/               # Config, parsing, requests
├── tests/
├── .env.example
├── pyproject.toml
└── README.md
```

---

## Development

**1. Clone the repository**

```bash
git clone https://github.com/Marin2409/footstats-cli.git
cd footstats-cli
```

**2. Install UV**

```bash
# macOS
brew install uv

# Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**3. Install dependencies**

```bash
uv sync
```

**4. Set up environment variables**

```bash
cp .env.example .env
```

**5. Run directly without installing**

```bash
# With Python
python -m src.cli.main [command] [argument]

# With UV (Recommended)
uv run python -m src.cli.main [command] [argument]
```

| Segment | Description |
|--------|-------------|
| `src` | Root source folder |
| `cli` | CLI parent folder |
| `main` | Entry point file |
| `command` | Action (e.g. `player`, `stats`) |
| `argument` | Player name (e.g. `"Cristiano"`) |

**Run Tests**

```bash
pytest tests/test_providers.py
```

---

## Disclaimer

This project is an independent open-source tool and is not affiliated with, endorsed by, or sponsored by [Transfermarkt](https://www.transfermarkt.com/) or any other data provider. Use it at your own risk and ensure compliance with their [Terms of Service](https://www.transfermarkt.com/intern/anb) and avoid excessive requests. The `REQUEST_DELAY` setting in `.env` helps ensure responsible usage.

Users are solely responsible for ensuring that their use of this software complies with applicable laws, regulations, website terms of service, robots.txt policies, and rate-limiting requirements.

The authors provide this software for educational and research purposes only and make no representations regarding the legality or appropriateness of its use in any particular jurisdiction or against any particular website.

---

## User Responsibility

By using this software, you acknowledge that you are responsible for determining whether your use complies with applicable laws, regulations, and the terms of service of any websites you access.

The authors are not responsible for how users choose to use this software.

---

## Contributing

Contributions are welcome! Please open an issue before submitting a pull request so we can discuss the change.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---

## License

MIT License — see [LICENSE](LICENSE) for details.