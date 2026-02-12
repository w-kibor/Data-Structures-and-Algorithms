"""Problem: Find the largest prime factor of a given integer."""

import sys


def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n."""
    n = abs(n)
    if n <= 1:
        return n
    largest = None
    while n % 2 == 0:
        largest = 2
        n //= 2
    p = 3
    while p * p <= n:
        while n % p == 0:
            largest = p
            n //= p
        p += 2
    if n > 1:
        largest = n
    return largest if largest is not None else n


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    print(largest_prime_factor(n))


if __name__ == "__main__":
    main()
