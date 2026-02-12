"""Problem: Find minimum moves to solve the 8-puzzle (or -1 if impossible)."""

import collections
import sys


goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def inversion_count(state) -> int:
    """Count inversions ignoring the blank (0)."""
    arr = [x for x in state if x != 0]
    inv = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inv += 1
    return inv


def is_solvable(state) -> bool:
    """3x3 puzzle is solvable when inversion count is even."""
    return inversion_count(state) % 2 == 0


def min_moves(start) -> int:
    """Return minimum number of moves to reach goal, or -1 if impossible."""
    if start == goal:
        return 0
    if not is_solvable(start):
        return -1

    neighbors = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4, 6],
        4: [1, 3, 5, 7],
        5: [2, 4, 8],
        6: [3, 7],
        7: [4, 6, 8],
        8: [5, 7],
    }

    queue = collections.deque([(start, 0)])
    seen = {start}
    while queue:
        state, dist = queue.popleft()
        zero_idx = state.index(0)
        for nxt in neighbors[zero_idx]:
            new_state = list(state)
            new_state[zero_idx], new_state[nxt] = new_state[nxt], new_state[zero_idx]
            new_state = tuple(new_state)
            if new_state in seen:
                continue
            if new_state == goal:
                return dist + 1
            seen.add(new_state)
            queue.append((new_state, dist + 1))
    return -1


def main() -> None:
    data = sys.stdin.read().strip().split()
    if len(data) < 9:
        return
    nums = tuple(map(int, data[:9]))
    print(min_moves(nums))


if __name__ == "__main__":
    main()
