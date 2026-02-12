"""Problem: Given three side lengths, check if they form a valid triangle."""

import sys


def is_valid_triangle(a: float, b: float, c: float) -> bool:
    return a > 0 and b > 0 and c > 0 and a + b >= c and a + c >= b and b + c >= a


def main() -> None:
    data = sys.stdin.read().strip().split()
    if len(data) < 3:
        return
    a, b, c = map(float, data[:3])
    print("true" if is_valid_triangle(a, b, c) else "false")


if __name__ == "__main__":
    main()
