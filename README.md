# Footstats-Scraper

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

