import sys


def is_armstrong(n: int) -> bool:
    if n < 0:
        return False
    s = str(n)
    power = len(s)
    total = 0
    for ch in s:
        total += int(ch) ** power
    return total == n


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    print("true" if is_armstrong(n) else "false")


if __name__ == "__main__":
    main()
