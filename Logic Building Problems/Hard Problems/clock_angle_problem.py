"""Problem: Compute the smaller angle between clock hands at a time."""

import sys


def clock_angle(hour: int, minute: int) -> float:
    """Return the smaller angle between hour and minute hands."""
    hour %= 12
    hour_angle = 30 * hour + 0.5 * minute
    minute_angle = 6 * minute
    diff = abs(hour_angle - minute_angle)
    return min(diff, 360 - diff)


def main() -> None:
    data = sys.stdin.read().strip().split()
    if len(data) < 2:
        return
    hour, minute = map(int, data[:2])
    angle = clock_angle(hour, minute)
    print(f"{angle:.6f}")


if __name__ == "__main__":
    main()
