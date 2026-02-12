"""Problem: Given an integer, output the number with its digits reversed."""

import sys


def reverse_digits(n: int) -> int:
    sign = -1 if n < 0 else 1
    s = str(abs(n))
    return sign * int(s[::-1])


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    print(reverse_digits(n))


if __name__ == "__main__":
    main()
