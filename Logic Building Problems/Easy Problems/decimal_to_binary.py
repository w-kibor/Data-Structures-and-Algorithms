import sys


def to_binary(n: int) -> str:
    if n == 0:
        return "0"
    sign = "-" if n < 0 else ""
    n = abs(n)
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    return sign + "".join(reversed(bits))


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    print(to_binary(n))


if __name__ == "__main__":
    main()
