import math
import sys


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.hypot(x2 - x1, y2 - y1)


def main() -> None:
    data = sys.stdin.read().strip().split()
    if len(data) < 4:
        return
    x1, y1, x2, y2 = map(float, data[:4])
    d = distance(x1, y1, x2, y2)
    print(f"{d:.6f}")


if __name__ == "__main__":
    main()
