"""Problem: Given an integer, determine whether it is a palindrome."""

import sys


def is_palindrome_number(n: int) -> bool:
    s = str(abs(n))
    return s == s[::-1]


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    print("true" if is_palindrome_number(n) else "false")


if __name__ == "__main__":
    main()
