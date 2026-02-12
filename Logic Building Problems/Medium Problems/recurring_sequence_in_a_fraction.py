"""Problem: Given a fraction, output the repeating decimal sequence."""

import sys


def recurring_sequence(numerator: int, denominator: int) -> str:
    """Return the repeating sequence of digits in numerator/denominator.

    If the decimal terminates, return an empty string.
    """
    if denominator == 0:
        raise ValueError("Denominator must be non-zero")
    numerator = abs(numerator)
    denominator = abs(denominator)
    remainder = numerator % denominator

    seen = {}
    digits = []
    idx = 0
    while remainder != 0 and remainder not in seen:
        seen[remainder] = idx
        remainder *= 10
        digit = remainder // denominator
        digits.append(str(digit))
        remainder %= denominator
        idx += 1

    if remainder == 0:
        return ""
    start = seen[remainder]
    return "".join(digits[start:])


def main() -> None:
    data = sys.stdin.read().strip().split()
    if len(data) < 2:
        return
    num, den = map(int, data[:2])
    print(recurring_sequence(num, den))


if __name__ == "__main__":
    main()
