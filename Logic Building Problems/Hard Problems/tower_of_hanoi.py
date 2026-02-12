"""Problem: Print the sequence of moves to solve Tower of Hanoi."""

import sys


def hanoi(n: int, source: str, auxiliary: str, target: str, moves):
    """Generate the move list for Tower of Hanoi."""
    if n == 0:
        return
    hanoi(n - 1, source, target, auxiliary, moves)
    moves.append(f"{source} -> {target}")
    hanoi(n - 1, auxiliary, source, target, moves)


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    moves = []
    hanoi(n, "A", "B", "C", moves)
    print("\n".join(moves))


if __name__ == "__main__":
    main()
