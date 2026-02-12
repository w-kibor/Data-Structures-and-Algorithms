"""Problem: Compute the binomial coefficient C(n, k)."""

import sys


def binomial_coefficient(n: int, k: int) -> int:
    """Compute C(n, k) using multiplicative formula."""
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    result = 1
    for i in range(1, k + 1):
        result = result * (n - k + i) // i
    return result


def main() -> None:
    data = sys.stdin.read().strip().split()
    if len(data) < 2:
        return
    n, k = map(int, data[:2])
    print(binomial_coefficient(n, k))


if __name__ == "__main__":
    main()
