"""Problem: Output the prime factorization of a given integer."""

import sys


def prime_factors(n: int):
    """Return prime factors as a list in non-decreasing order."""
    n = abs(n)
    factors = []
    while n % 2 == 0 and n > 0:
        factors.append(2)
        n //= 2
    p = 3
    while p * p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p
        p += 2
    if n > 1:
        factors.append(n)
    return factors


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    factors_list = prime_factors(n)
    print(" ".join(map(str, factors_list)))


if __name__ == "__main__":
    main()
