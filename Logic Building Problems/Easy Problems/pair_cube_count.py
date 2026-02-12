import sys


def integer_cuberoot(n: int) -> int:
    if n < 0:
        return -integer_cuberoot(-n)
    x = int(round(n ** (1 / 3)))
    while (x + 1) ** 3 <= n:
        x += 1
    while x ** 3 > n:
        x -= 1
    return x


def pair_cube_count(n: int) -> int:
    if n < 0:
        return 0
    count = 0
    limit = integer_cuberoot(n)
    for a in range(0, limit + 1):
        a3 = a ** 3
        b3 = n - a3
        b = integer_cuberoot(b3)
        if b >= a and b ** 3 == b3:
            count += 1
    return count


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    print(pair_cube_count(n))


if __name__ == "__main__":
    main()
