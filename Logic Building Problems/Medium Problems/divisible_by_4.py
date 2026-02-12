"""Problem: Determine whether the given integer is divisible by 4."""

import sys


def is_divisible_by_4(s: str) -> bool:
    """Check divisibility by 4 using last two digits.

    For short strings, use the whole number.
    """
    if not s:
        return False
    if s[0] == '-':
        s = s[1:]
    if len(s) <= 2:
        return int(s) % 4 == 0
    return int(s[-2:]) % 4 == 0


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    s = data[0]
    print("true" if is_divisible_by_4(s) else "false")


if __name__ == "__main__":
    main()
