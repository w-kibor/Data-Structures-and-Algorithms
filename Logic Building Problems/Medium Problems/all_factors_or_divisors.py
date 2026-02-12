"""Problem: List all positive factors (divisors) of a given integer."""

import sys


def factors(n: int):
    """Return all positive factors of n in sorted order."""
    if n == 0:
        return []
    n = abs(n)
    small = []
    large = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            small.append(i)
            if i * i != n:
                large.append(n // i)
        i += 1
    return small + large[::-1]


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    print(" ".join(map(str, factors(n))))


if __name__ == "__main__":
    main()
