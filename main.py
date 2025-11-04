"""
Example usage of the chrono_simplex timing package.
"""

import time

from chrono_simplex import Timer, format_time, setup_logging


def main():
    # Set up logging to stdout
    setup_logging()

    print("=" * 60)
    print("Examples with human-readable formatting (default)")
    print("=" * 60)

    # Example 1: Basic usage with default label
    with Timer():
        time.sleep(0.5)

    # Example 2: Custom label
    with Timer("Database query"):
        time.sleep(0.3)

    # Example 3: Timing a computation
    with Timer("Complex calculation"):
        result = sum(i**2 for i in range(1000000))
        print(f"Result: {result}")

    # Example 4: Very short duration (milliseconds)
    with Timer("Quick operation"):
        time.sleep(0.001)

    # Example 5: Longer duration (minutes)
    with Timer("Long operation"):
        time.sleep(65)  # 1 minute 5 seconds

    # Example 6: Nested timers
    with Timer("Outer operation"):
        time.sleep(0.2)
        with Timer("Inner operation"):
            time.sleep(0.1)
        time.sleep(0.2)

    print("\n" + "=" * 60)
    print("Examples with raw seconds (use_formatter=False)")
    print("=" * 60)

    # Example 7: Raw seconds format
    with Timer("Raw format example", use_formatter=False):
        time.sleep(0.123)

    print("\n" + "=" * 60)
    print("Direct formatter usage")
    print("=" * 60)

    # Example 8: Using the formatter directly
    print(f"0.001 seconds = {format_time(0.001)}")
    print(f"0.5 seconds = {format_time(0.5)}")
    print(f"65 seconds = {format_time(65)}")
    print(f"3661 seconds = {format_time(3661)}")
    print(f"86400 seconds = {format_time(86400)}")
    print(f"604800 seconds = {format_time(604800)}")
    print(f"2629800 seconds = {format_time(2629800)}")
    print(f"31557600 seconds = {format_time(31557600)}")


if __name__ == "__main__":
    main()
