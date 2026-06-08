<!-- # Footstats-Scraper

Manage Football Stats from the your own Terminal CLI.  

---

## Web Scraping Sources 

| Markdown    | Source              | What to expect | 
|--------|----------------------|--------|
| [Transfermarkt](/docs/transfermarkt.md) | [Link to Website](https://www.transfermarkt.com/) |Player Market Value, Transfers, Matches Played, Penalties, etc | 

## Package Management
This project uses [UV](https://github.com/astral-sh/uv) as the Python package manager and environment manager. UV is a fast, modern alternative to pip and virtualenv.

**UV Environments:** The `root` directory is configured as a UV project with its own virtual environment and dependencies.

#### UV Installation Steps
```bash
# Install UV (if not already installed)
brew install uv  # macOS
# or: curl -LsSf https://astral.sh/uv/install.sh | sh  # Linux/macOS
# or: powershell -c "irm https://astral.sh/uv/install.ps1 | iex"  # Windows

# Install base dependencies only
uv sync

# OR install everything (all optional dependencies)
uv sync --all-extras
```

#### Activate the Virtual Environment

**Using VSCODE Command Pallete**
```bash
# Get Python interpreter path for VSCode
uv run which python

# In VSCode:
# 1. Cmd+Shift+P (Mac) or Ctrl+Shift+P (Windows/Linux)
# 2. Type "Python: Select Interpreter"
# 3. Paste the path from above
# 4. Create a new terminal (Cmd+Shift+P -> "Create New Terminal with Profile")
```

**In terminal**
Activate the new virtual environment so that any Python command you run or package you install uses it.

```bash 
source .venv/bin/activate
```

Every time you install a new package in that environment, activate the environment again.

This makes sure that if you use a terminal (CLI) program installed by that package, you use the one from your virtual environment and not any other that could be installed globally, probably with a different version than what you need.
 -->

# Footstats CLI

> Football player stats, transfers, and market values — straight from your terminal.
[![License: MIT](https://img.shields.io/github/license/Marin2409/footstats-scraper)](LICENSE)
![UV](https://img.shields.io/badge/package%20manager-uv-purple?style=flat)
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

- Python 3.13+
- [UV](https://github.com/astral-sh/uv) package manager

---

## Installation

**1. Install UV**

```bash
# macOS
brew install uv

# Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**2. Clone the repository**

```bash
git clone https://github.com/yourusername/footstats-scraper.git
cd footstats-scraper
```

**3. Install dependencies**

```bash
uv sync
```

**4. Set up environment variables**

```bash
cp .env.example .env
```

**5. Activate the Virtual Environment**

```bash
# Get Python interpreter path for VSCode
uv run which python
```

**Using VSCODE Command Pallete:**
1.  Cmd+Shift+P (Mac) or Ctrl+Shift+P (Windows/Linux)
2.  Type "Python: Select Interpreter"
3.  Paste the path from above
4.  Create a new terminal (Cmd+Shift+P -> "Create New Terminal with Profile")


**In terminal**
Activate the new virtual environment so that any Python command you run or package you install uses it.

```bash 
source .venv/bin/activate
```

Every time you install a new package in that environment, activate the environment again.

This makes sure that if you use a terminal (CLI) program installed by that package, you use the one from your virtual environment and not any other that could be installed globally, probably with a different version than what you need.

**5. Install the CLI**

```bash
uv pip install -e .
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

Copy `.env.example` to `.env` and adjust as needed:

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

**Run with Python:**
```python
# Run directly with python without installing
python -m src.cli.main [command] [argument]
```

**Run with UV:**
```bash
# Run directly with uv without installing
uv run python -m src.cli.main [command] [arguments]
```

| "scr"    | "cli"              | "main" | "command" | "argument |
|--------|----------------------|--------|-----------|-----------|
| Root | Parent Folder | File you wanna run | Action | Passing argument, Ex. "cristiano" |

**Run Tests**
```bash
# Run tests
pytest tests/test_providers.py ..
```

---

## Disclaimer

This project is for educational purposes only. Data is sourced from [Transfermarkt](https://www.transfermarkt.com/). Please respect their [Terms of Service](https://www.transfermarkt.com/intern/anb) and avoid excessive requests. The `REQUEST_DELAY` setting in `.env` helps ensure responsible usage.

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