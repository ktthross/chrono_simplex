"""
Timer context manager for measuring execution time.
"""

import logging
import time
from dataclasses import dataclass

from .formatter import format_time

logger = logging.getLogger(__name__)


@dataclass
class TimingData:
    raw_time: float
    formatted_time: str


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

    def get_timing_data(self) -> TimingData:
        """
        Get current timing data without stopping the timer.

        Returns:
            TimingData with raw_time (float) and formatted_time (str)
        """
        if self.start_time is None:
            raise RuntimeError("Timer has not been started")

        current_time = time.perf_counter()
        elapsed = current_time - self.start_time

        return TimingData(raw_time=elapsed, formatted_time=format_time(elapsed))

    def stop_and_get_timing_data(self) -> TimingData:
        """
        Stop the timer and return timing data.

        Returns:
            TimingData with raw_time (float) and formatted_time (str)
        """
        if self.start_time is None:
            raise RuntimeError("Timer has not been started")

        self.end_time = time.perf_counter()
        self.elapsed_time = self.end_time - self.start_time

        return TimingData(raw_time=self.elapsed_time, formatted_time=format_time(self.elapsed_time))
