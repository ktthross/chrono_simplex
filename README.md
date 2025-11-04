# chrono_simplex

A simple Python timing package with context manager support and minimal dependencies.

> **Note:** This is a personal project for private use. Not published to PyPI.

## Features

- ⏱️ Context manager for easy timing of code blocks
- 📝 Built-in logging support with configurable output
- 🎯 Zero external dependencies (uses only Python standard library)
- 🔧 Simple and intuitive API
- 📊 Human-readable time formatting (years, months, weeks, days, hours, minutes, seconds, milliseconds)
- 🛠️ Pre-commit hooks with Ruff for code quality
- 💻 VSCode integration with format-on-save

## Installation

This package is managed by [uv](https://github.com/astral-sh/uv).

### Quick Start

```bash
# Clone the repository
git clone https://github.com/ktthross/chrono_simplex.git
cd chrono_simplex

# Install dependencies (creates virtual environment automatically)
uv sync --dev

# Install pre-commit hooks
uv run pre-commit install
```

For detailed setup instructions, including how to regenerate the lock file without private registry references, see [SETUP.md](SETUP.md).

### Direct from GitHub (without cloning)

```bash
uv pip install git+https://github.com/ktthross/chrono_simplex.git
```

## Usage

### Basic Example

```python
from chrono_simplex import Timer, setup_logging

# Set up logging to stdout
setup_logging()

# Time a code block with a custom label
with Timer("My operation"):
    # Your code here
    pass
```

### Examples

```python
import time
from chrono_simplex import Timer, setup_logging, format_time

# Set up logging
setup_logging()

# Example 1: Basic usage with default label (human-readable format)
with Timer():
    time.sleep(0.5)

# Example 2: Custom label
with Timer("Database query"):
    time.sleep(0.3)

# Example 3: Very short duration (milliseconds)
with Timer("Quick operation"):
    time.sleep(0.001)

# Example 4: Longer duration (minutes)
with Timer("Long operation"):
    time.sleep(65)  # 1 minute 5 seconds

# Example 5: Raw seconds format
with Timer("Raw format", use_formatter=False):
    time.sleep(0.123)

# Example 6: Using the formatter directly
print(format_time(0.001))   # "1.000 millisecond"
print(format_time(65))      # "1 minute 5 seconds"
print(format_time(3661))    # "1 hour 1 minute 1 second"
```

### Output

```text
2025-11-04 11:58:51,909 - chrono_simplex.timer - INFO - Test: Starting...
2025-11-04 11:58:52,013 - chrono_simplex.timer - INFO - Test: Completed in 104.111 milliseconds
```

## API Reference

### `Timer(label: str | None = None, use_formatter: bool = True)`

A context manager for timing code execution.

**Parameters:**

- `label` (str, optional): A string that will be printed at the beginning of the output. Defaults to "Execution".
- `use_formatter` (bool, optional): If True, formats time in human-readable format. If False, shows raw seconds. Defaults to True.

**Attributes:**

- `elapsed_time` (float): The elapsed time in seconds (available after context exits)

### `format_time(seconds: float) -> str`

Format time in seconds to a human-readable string.

**Parameters:**

- `seconds` (float): Time in seconds (can be fractional)

**Returns:**

- A formatted string showing time in years, months, weeks, days, hours, minutes, seconds, and milliseconds (only non-zero values are shown)

### `setup_logging(level: int = logging.INFO, format_string: str = None)`

Configure logging to write to stdout.

**Parameters:**

- `level` (int, optional): The logging level. Defaults to `logging.INFO`.
- `format_string` (str, optional): Custom format string for log messages. If not provided, uses a default format with timestamp.

## Development

### Requirements

- Python >= 3.11
- No runtime dependencies
- Dev dependencies: `ruff`, `pre-commit`

### Setup

```bash
# Install dev dependencies
uv sync --dev

# Install pre-commit hooks
uv run pre-commit install

# Run linting and formatting
uv run ruff check --fix .
uv run ruff format .

# Run pre-commit on all files
uv run pre-commit run --all-files
```

### VSCode Integration

The project includes VSCode settings that:
- Use Ruff as the default Python formatter
- Format code on save
- Organize imports on save
- Run linting automatically

Make sure to install the recommended Ruff extension (`charliermarsh.ruff`).

## Contributing

This is a personal project, but if you'd like to suggest improvements:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run the linting and formatting checks (`uv run ruff check --fix . && uv run ruff format .`)
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
