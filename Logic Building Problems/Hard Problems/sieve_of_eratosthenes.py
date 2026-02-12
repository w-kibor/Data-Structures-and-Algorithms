"""Problem: List all primes up to n using the Sieve of Eratosthenes."""

import sys


def sieve(n: int):
    """Return all primes <= n using the sieve of Eratosthenes."""
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0:2] = [False, False]
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
        p += 1
    return [i for i, flag in enumerate(is_prime) if flag]


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    primes = sieve(n)
    print(" ".join(map(str, primes)))


if __name__ == "__main__":
    main()
