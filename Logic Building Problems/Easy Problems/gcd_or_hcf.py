"""Problem: Given two integers, output their GCD (HCF)."""

import math
import sys


def main() -> None:
    data = sys.stdin.read().strip().split()
    if len(data) < 2:
        return
    a, b = map(int, data[:2])
    print(math.gcd(a, b))


if __name__ == "__main__":
    main()
