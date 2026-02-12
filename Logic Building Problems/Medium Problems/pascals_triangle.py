"""Problem: Generate Pascal's triangle up to a given number of rows."""

import sys


def generate_pascals_triangle(rows: int):
    """Generate Pascal's triangle up to the given number of rows."""
    triangle = []
    for r in range(rows):
        if r == 0:
            triangle.append([1])
            continue
        prev = triangle[-1]
        row = [1]
        for i in range(1, r):
            row.append(prev[i - 1] + prev[i])
        row.append(1)
        triangle.append(row)
    return triangle


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    rows = int(data[0])
    triangle = generate_pascals_triangle(rows)
    for row in triangle:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()
