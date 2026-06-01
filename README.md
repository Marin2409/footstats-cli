# Footstats-Scraper

## Package Management
This project uses [UV](https://github.com/astral-sh/uv) as the Python package manager and environment manager. UV is a fast, modern alternative to pip and virtualenv.

### UV Environments
The `root` directory is configured as a UV project with its own virtual environment and dependencies.

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

#### VSCode Setup
```bash
# Get Python interpreter path for VSCode
uv run which python

# In VSCode:
# 1. Cmd+Shift+P (Mac) or Ctrl+Shift+P (Windows/Linux)
# 2. Type "Python: Select Interpreter"
# 3. Paste the path from above
# 4. Create a new terminal (Cmd+Shift+P -> "Create New Terminal with Profile")
```

### Run main.py

Run with python:
```python -m src.cli.main```

Run with uv:
```uv run python -m src.cli.main```

