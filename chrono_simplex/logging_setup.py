"""
Logging configuration for chrono_simplex.
"""

import logging
import sys


def setup_logging(level: int = logging.INFO, format_string: str = None) -> None:
    """
    Configure logging to write to stdout.

    Args:
        level: The logging level (default: logging.INFO)
        format_string: Custom format string for log messages.
                      If not provided, uses a default format with timestamp.
    """
    if format_string is None:
        format_string = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # Create a handler that writes to stdout
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)

    # Create a formatter
    formatter = logging.Formatter(format_string)
    handler.setFormatter(formatter)

    # Get the root logger and configure it
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    # Remove any existing handlers to avoid duplicates
    root_logger.handlers.clear()

    # Add our handler
    root_logger.addHandler(handler)
