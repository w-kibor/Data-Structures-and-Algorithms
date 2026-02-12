import sys


def is_perfect_number(n: int) -> bool:
    if n <= 1:
        return False
    total = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            other = n // i
            if other != i:
                total += other
        i += 1
    return total == n


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    print("true" if is_perfect_number(n) else "false")


if __name__ == "__main__":
    main()
