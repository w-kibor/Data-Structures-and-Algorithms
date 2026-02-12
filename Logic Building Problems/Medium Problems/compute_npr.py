"""Problem: Compute nPr for given n and r."""

import sys


def npr(n: int, r: int) -> int:
    """Compute nPr = n! / (n-r)! using a product to avoid big factorials."""
    if r < 0 or r > n:
        return 0
    result = 1
    for i in range(n - r + 1, n + 1):
        result *= i
    return result


def main() -> None:
    data = sys.stdin.read().strip().split()
    if len(data) < 2:
        return
    n, r = map(int, data[:2])
    print(npr(n, r))


if __name__ == "__main__":
    main()
