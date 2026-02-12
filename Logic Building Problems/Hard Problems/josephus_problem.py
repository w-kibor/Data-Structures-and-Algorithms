"""Problem: Compute the survivor position in the Josephus problem."""

import sys


def josephus(n: int, k: int) -> int:
    """Return the 1-based survivor position using iterative solution."""
    if n <= 0 or k <= 0:
        return 0
    survivor = 0
    for i in range(1, n + 1):
        survivor = (survivor + k) % i
    return survivor + 1


def main() -> None:
    data = sys.stdin.read().strip().split()
    if len(data) < 2:
        return
    n, k = map(int, data[:2])
    print(josephus(n, k))


if __name__ == "__main__":
    main()
