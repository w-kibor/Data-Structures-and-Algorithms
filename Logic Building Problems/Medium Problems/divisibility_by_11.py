"""Problem: Determine whether the given integer is divisible by 11."""

import sys


def is_divisible_by_11(s: str) -> bool:
    """Use alternating sum rule for divisibility by 11."""
    if not s:
        return False
    if s[0] == '-':
        s = s[1:]
    odd_sum = 0
    even_sum = 0
    for idx, ch in enumerate(s):
        digit = ord(ch) - ord('0')
        if idx % 2 == 0:
            odd_sum += digit
        else:
            even_sum += digit
    return (odd_sum - even_sum) % 11 == 0


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    s = data[0]
    print("true" if is_divisible_by_11(s) else "false")


if __name__ == "__main__":
    main()
