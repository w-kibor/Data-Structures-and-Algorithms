import math
import sys


def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // math.gcd(a, b)


def main() -> None:
    data = sys.stdin.read().strip().split()
    if len(data) < 2:
        return
    a, b = map(int, data[:2])
    print(lcm(a, b))


if __name__ == "__main__":
    main()
