"""
Timer context manager for measuring execution time.
"""

import logging
import time

from .formatter import format_time

logger = logging.getLogger(__name__)


class Timer:
    """
    A context manager for timing code execution.

    Usage:
        with Timer("Operation name"):
            # code to time
            pass

    Args:
        label: A string that will be printed at the beginning of the output.
               If not provided, defaults to "Execution".
    """

    def __init__(self, label: str | None = None, use_formatter: bool = True):
        """
        Initialize the Timer context manager.

        Args:
            label: Optional label to identify the timed operation.
            use_formatter: If True, formats time in human-readable format.
                          If False, shows time in seconds with 6 decimal places.
        """
        self.label = label or "Execution"
        self.use_formatter = use_formatter
        self.start_time: float | None = None
        self.end_time: float | None = None
        self.elapsed_time: float | None = None

    def __enter__(self):
        """Start the timer when entering the context."""
        self.start_time = time.perf_counter()
        logger.info(f"{self.label}: Starting...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Stop the timer and log the elapsed time when exiting the context."""
        self.end_time = time.perf_counter()
        self.elapsed_time = self.end_time - self.start_time

        if self.use_formatter:
            time_str = format_time(self.elapsed_time)
            logger.info(f" {self.label}: Completed in {time_str}")
        else:
            logger.info(f" {self.label}: Completed in {self.elapsed_time:.6f} seconds")

        return False  # Don't suppress exceptions
