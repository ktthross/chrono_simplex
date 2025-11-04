"""
Time formatting utilities for human-readable time display.
"""


def format_time(seconds: float) -> str:
    """
    Format time in seconds to a human-readable string.

    Displays time in delineations of years, months, weeks, days, hours,
    minutes, seconds, and milliseconds. Only shows non-zero values.

    Args:
        seconds: Time in seconds (can be fractional)

    Returns:
        A formatted string like "2 hours 3 minutes 45.123 seconds"
        or "123.456 milliseconds" for very short durations.

    Examples:
        >>> format_time(0.001234)
        '1.234 milliseconds'
        >>> format_time(90)
        '1 minute 30 seconds'
        >>> format_time(3661)
        '1 hour 1 minute 1 second'
        >>> format_time(86400 * 365)
        '1 year'
    """
    if seconds == 0:
        return "0 seconds"

    # Time unit definitions in seconds
    YEAR = 365.25 * 24 * 60 * 60  # Account for leap years
    MONTH = 30.44 * 24 * 60 * 60  # Average month length
    WEEK = 7 * 24 * 60 * 60
    DAY = 24 * 60 * 60
    HOUR = 60 * 60
    MINUTE = 60
    SECOND = 1
    MILLISECOND = 0.001

    parts = []
    remaining = abs(seconds)  # Work with absolute value

    # Years
    if remaining >= YEAR:
        years = int(remaining // YEAR)
        parts.append(f"{years} {'year' if years == 1 else 'years'}")
        remaining %= YEAR

    # Months
    if remaining >= MONTH:
        months = int(remaining // MONTH)
        parts.append(f"{months} {'month' if months == 1 else 'months'}")
        remaining %= MONTH

    # Weeks
    if remaining >= WEEK:
        weeks = int(remaining // WEEK)
        parts.append(f"{weeks} {'week' if weeks == 1 else 'weeks'}")
        remaining %= WEEK

    # Days
    if remaining >= DAY:
        days = int(remaining // DAY)
        parts.append(f"{days} {'day' if days == 1 else 'days'}")
        remaining %= DAY

    # Hours
    if remaining >= HOUR:
        hours = int(remaining // HOUR)
        parts.append(f"{hours} {'hour' if hours == 1 else 'hours'}")
        remaining %= HOUR

    # Minutes
    if remaining >= MINUTE:
        minutes = int(remaining // MINUTE)
        parts.append(f"{minutes} {'minute' if minutes == 1 else 'minutes'}")
        remaining %= MINUTE

    # Seconds and milliseconds
    if remaining >= SECOND:
        # Show seconds with decimal places if there are fractional seconds
        if remaining != int(remaining):
            parts.append(f"{remaining:.3f} seconds")
        else:
            secs = int(remaining)
            parts.append(f"{secs} {'second' if secs == 1 else 'seconds'}")
    elif remaining > 0:
        # Less than 1 second - show as milliseconds
        milliseconds = remaining / MILLISECOND
        parts.append(f"{milliseconds:.3f} {'millisecond' if milliseconds == 1 else 'milliseconds'}")

    result = " ".join(parts)

    # Add negative sign if original value was negative
    if seconds < 0:
        result = f"-{result}"

    return result if result else "0 seconds"
