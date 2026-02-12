"""Problem: Compute (a^b) mod m efficiently."""

import sys


def mod_pow(a: int, b: int, m: int) -> int:
    """Compute (a^b) mod m using fast exponentiation."""
    if m == 0:
        raise ValueError("modulus must be non-zero")
    result = 1 % m
    base = a % m
    exp = b
    while exp > 0:
        if exp & 1:
            result = (result * base) % m
        base = (base * base) % m
        exp >>= 1
    return result


def main() -> None:
    data = sys.stdin.read().strip().split()
    if len(data) < 3:
        return
    a, b, m = map(int, data[:3])
    print(mod_pow(a, b, m))


if __name__ == "__main__":
    main()
