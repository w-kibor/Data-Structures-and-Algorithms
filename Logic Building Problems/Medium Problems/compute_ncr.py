"""Problem: Compute nCr for given n and r."""

import sys


def ncr(n: int, r: int) -> int:
    """Compute nCr using multiplicative formula with symmetry."""
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    result = 1
    for i in range(1, r + 1):
        result = result * (n - r + i) // i
    return result


def main() -> None:
    data = sys.stdin.read().strip().split()
    if len(data) < 2:
        return
    n, r = map(int, data[:2])
    print(ncr(n, r))


if __name__ == "__main__":
    main()
