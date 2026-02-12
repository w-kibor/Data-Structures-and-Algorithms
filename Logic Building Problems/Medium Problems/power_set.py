"""Problem: Generate the power set of a list of items."""

import sys


def power_set(items):
    """Generate all subsets of the given list."""
    n = len(items)
    subsets = []
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(items[i])
        subsets.append(subset)
    return subsets


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    items = data
    subsets = power_set(items)
    for subset in subsets:
        print(" ".join(subset))


if __name__ == "__main__":
    main()
