"""Problem: Find the k-th digit (from right) of a^b."""

import sys


def kth_digit_of_power(a: int, b: int, k: int) -> int:
    """Return the k-th digit (from right, 1-indexed) of a^b.

    Uses fast exponentiation with modular reduction by 10^k.
    """
    if k <= 0:
        raise ValueError("k must be positive")
    mod = 10 ** k
    result = 1
    base = a % mod
    exp = b
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return (result // (10 ** (k - 1))) % 10


def main() -> None:
    data = sys.stdin.read().strip().split()
    if len(data) < 3:
        return
    a, b, k = map(int, data[:3])
    print(kth_digit_of_power(a, b, k))


if __name__ == "__main__":
    main()
