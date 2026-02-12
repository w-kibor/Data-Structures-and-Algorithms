"""Problem: Given a non-negative integer, output floor(sqrt(n))."""

import sys


def integer_sqrt(n: int) -> int:
    """Return floor(sqrt(n)) for n >= 0 using binary search."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    left, right = 1, n // 2
    ans = 1
    while left <= right:
        mid = (left + right) // 2
        sq = mid * mid
        if sq == n:
            return mid
        if sq < n:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    print(integer_sqrt(n))


if __name__ == "__main__":
    main()
