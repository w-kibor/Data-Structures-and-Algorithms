"""Problem: Convert a fraction to a decimal string with repeating parts."""

import sys


def fraction_to_decimal(numerator: int, denominator: int) -> str:
    """Convert fraction to string with repeating part in parentheses."""
    if denominator == 0:
        raise ValueError("Denominator must be non-zero")
    if numerator == 0:
        return "0"
    sign = "-" if (numerator < 0) ^ (denominator < 0) else ""
    numerator = abs(numerator)
    denominator = abs(denominator)

    integer_part = numerator // denominator
    remainder = numerator % denominator
    if remainder == 0:
        return sign + str(integer_part)

    digits = []
    seen = {}
    idx = 0
    while remainder != 0 and remainder not in seen:
        seen[remainder] = idx
        remainder *= 10
        digit = remainder // denominator
        digits.append(str(digit))
        remainder %= denominator
        idx += 1

    if remainder == 0:
        frac = "".join(digits)
    else:
        repeat_start = seen[remainder]
        non_repeat = "".join(digits[:repeat_start])
        repeat = "".join(digits[repeat_start:])
        frac = f"{non_repeat}({repeat})"
    return f"{sign}{integer_part}.{frac}"


def main() -> None:
    data = sys.stdin.read().strip().split()
    if len(data) < 2:
        return
    num, den = map(int, data[:2])
    print(fraction_to_decimal(num, den))


if __name__ == "__main__":
    main()
