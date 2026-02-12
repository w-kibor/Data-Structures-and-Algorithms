"""Problem: Given two axis-aligned rectangles, determine if they overlap."""

import sys


def rectangles_overlap(r1, r2) -> bool:
    x1, y1, x2, y2 = r1
    x3, y3, x4, y4 = r2
    return not (x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1)


def main() -> None:
    data = sys.stdin.read().strip().split()
    if len(data) < 8:
        return
    nums = list(map(float, data[:8]))
    r1 = nums[0:4]
    r2 = nums[4:8]
    print("true" if rectangles_overlap(r1, r2) else "false")


if __name__ == "__main__":
    main()
