"""Problem: Determine if a number is super prime (prime and digit-sum prime)."""

import sys


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def digit_sum(n: int) -> int:
    total = 0
    n = abs(n)
    while n > 0:
        total += n % 10
        n //= 10
    return total


def is_super_prime(n: int) -> bool:
    """Super prime: n is prime and its digit sum is also prime."""
    return is_prime(n) and is_prime(digit_sum(n))


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    print("true" if is_super_prime(n) else "false")


if __name__ == "__main__":
    main()
