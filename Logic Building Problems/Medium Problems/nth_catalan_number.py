"""Problem: Compute the n-th Catalan number."""

import sys


def catalan(n: int) -> int:
    """Compute the n-th Catalan number using DP."""
    if n < 0:
        raise ValueError("n must be non-negative")
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        total = 0
        for j in range(i):
            total += dp[j] * dp[i - 1 - j]
        dp[i] = total
    return dp[n]


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    print(catalan(n))


if __name__ == "__main__":
    main()
