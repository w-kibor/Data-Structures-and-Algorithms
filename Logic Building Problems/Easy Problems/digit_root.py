"""Problem: Given an integer, compute its digital root."""

import sys


def digit_root(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 0
    return 1 + (n - 1) % 9


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    print(digit_root(n))


if __name__ == "__main__":
    main()
