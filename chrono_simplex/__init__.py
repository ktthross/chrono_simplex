"""
chrono_simplex - A simple timing package with context manager support.
"""

from .formatter import format_time
from .logging_setup import setup_logging
from .timer import Timer

__version__ = "0.1.0"
__all__ = ["Timer", "setup_logging", "format_time"]
