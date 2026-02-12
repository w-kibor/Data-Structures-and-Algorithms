"""Problem: Compute Euler's totient function phi(n)."""

import sys


def phi(n: int) -> int:
    """Compute Euler's totient function using prime factorization."""
    if n == 0:
        return 0
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1 if p == 2 else 2
    if n > 1:
        result -= result // n
    return result


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    print(phi(n))


if __name__ == "__main__":
    main()
