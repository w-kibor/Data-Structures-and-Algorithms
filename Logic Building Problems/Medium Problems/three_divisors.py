"""Problem: Count numbers <= n that have exactly three divisors."""

import sys


def count_numbers_with_three_divisors(n: int) -> int:
    """Count numbers <= n that have exactly 3 divisors.

    A number has exactly 3 divisors iff it is a square of a prime.
    So count primes p where p^2 <= n.
    """
    if n < 4:
        return 0
    limit = int(n ** 0.5)
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            step = i
            start = i * i
            is_prime[start:limit + 1:step] = [False] * (((limit - start) // step) + 1)
    return sum(1 for i in range(2, limit + 1) if is_prime[i])


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    print(count_numbers_with_three_divisors(n))


if __name__ == "__main__":
    main()
