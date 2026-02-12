"""Problem: Determine whether the given integer is divisible by 13."""

import sys


def is_divisible_by_13(s: str) -> bool:
    """Check divisibility by 13 by computing modulo iteratively."""
    if not s:
        return False
    if s[0] == '-':
        s = s[1:]
    mod = 0
    for ch in s:
        mod = (mod * 10 + (ord(ch) - ord('0'))) % 13
    return mod == 0


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    s = data[0]
    print("true" if is_divisible_by_13(s) else "false")


if __name__ == "__main__":
    main()
