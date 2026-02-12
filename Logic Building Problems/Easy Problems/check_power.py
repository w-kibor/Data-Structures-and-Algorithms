"""Problem: Determine whether the given integer is a power of two."""

import sys


def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    print("true" if is_power_of_two(n) else "false")


if __name__ == "__main__":
    main()
