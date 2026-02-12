"""Problem: Compute max bottles distinguishable with rats and rounds."""

import sys


def max_bottles(rats: int, rounds: int) -> int:
    """Max bottles identifiable with given rats and rounds.

    Each rat has (rounds + 1) possible outcomes (dies in a round or survives).
    """
    if rats < 0 or rounds < 0:
        return 0
    return (rounds + 1) ** rats


def main() -> None:
    data = sys.stdin.read().strip().split()
    if len(data) < 2:
        return
    rats, rounds = map(int, data[:2])
    print(max_bottles(rats, rounds))


if __name__ == "__main__":
    main()
