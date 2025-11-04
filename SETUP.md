# Setup Instructions

## Initial Setup

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

### 1. Install UV

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Clone the Repository

```bash
git clone https://github.com/yourusername/chrono_simplex.git
cd chrono_simplex
```

### 3. Install Dependencies

```bash
# This will create a virtual environment and install all dependencies
uv sync --dev
```

### 4. Install Pre-commit Hooks

```bash
uv run pre-commit install
```

## Regenerating the Lock File

If you need to regenerate `uv.lock` to remove any JFrog or other private registry references:

```bash
# Remove the old lock file
rm uv.lock

# Regenerate with PyPI as the source
# Make sure you don't have any custom index configured in ~/.config/uv/uv.toml
# or temporarily rename that file
uv lock

# Reinstall dependencies
uv sync --dev
```

## Development Workflow

### Running the Example

```bash
python main.py
```

### Formatting and Linting

```bash
# Check for issues
uv run ruff check .

# Fix issues automatically
uv run ruff check --fix .

# Format code
uv run ruff format .
```

### Running Pre-commit Hooks Manually

```bash
uv run pre-commit run --all-files
```

## VSCode Setup

1. Install the recommended Ruff extension: `charliermarsh.ruff`
2. The project includes `.vscode/settings.json` which will:
   - Format code on save
   - Organize imports on save
   - Run linting automatically

## Troubleshooting

### JFrog References in uv.lock

If you see JFrog references in `uv.lock`, it means you have a global UV configuration pointing to a private registry.

**Solution:**

1. Check for global config: `cat ~/.config/uv/uv.toml`
2. Temporarily rename it: `mv ~/.config/uv/uv.toml ~/.config/uv/uv.toml.bak`
3. Regenerate the lock file: `rm uv.lock && uv lock`
4. Restore your global config: `mv ~/.config/uv/uv.toml.bak ~/.config/uv/uv.toml`

Alternatively, you can create a local `uv.toml` in the project root to override the global config:

```toml
[[index]]
name = "pypi"
url = "https://pypi.org/simple"
default = true
```

Then run `uv lock` to regenerate the lock file.

