import sys


def nth_triangular(n: int) -> int:
    return n * (n + 1) // 2


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    print(nth_triangular(n))


if __name__ == "__main__":
    main()
