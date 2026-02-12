"""Problem: Given n, output the n-th Fibonacci number."""

import sys


def fib(n: int) -> int:
    def helper(k: int):
        if k == 0:
            return 0, 1
        a, b = helper(k // 2)
        c = a * (2 * b - a)
        d = a * a + b * b
        if k % 2 == 0:
            return c, d
        return d, c + d

    return helper(n)[0]


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    print(fib(n))


if __name__ == "__main__":
    main()
