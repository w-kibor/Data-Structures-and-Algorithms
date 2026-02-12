import math
import sys


def add_fractions(a: int, b: int, c: int, d: int):
    if b == 0 or d == 0:
        raise ValueError("Denominator must be non-zero")
    num = a * d + c * b
    den = b * d
    g = math.gcd(num, den)
    num //= g
    den //= g
    if den < 0:
        num *= -1
        den *= -1
    return num, den


def main() -> None:
    data = sys.stdin.read().strip().split()
    if len(data) < 4:
        return
    a, b, c, d = map(int, data[:4])
    num, den = add_fractions(a, b, c, d)
    print(f"{num}/{den}")


if __name__ == "__main__":
    main()
