"""Problem: Given a date, output the corresponding day of the week."""

import datetime
import sys


def day_of_week(year: int, month: int, day: int) -> str:
    return datetime.date(year, month, day).strftime("%A")


def main() -> None:
    data = sys.stdin.read().strip().split()
    if len(data) < 3:
        return
    year, month, day = map(int, data[:3])
    print(day_of_week(year, month, day))


if __name__ == "__main__":
    main()
