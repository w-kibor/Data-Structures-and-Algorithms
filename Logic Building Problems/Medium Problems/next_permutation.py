"""Problem: Transform a sequence into its next lexicographic permutation."""

import sys


def next_permutation(nums):
    """Transform list into next lexicographic permutation.

    Returns False if it was the last permutation, True otherwise.
    """
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i < 0:
        nums.reverse()
        return False
    j = len(nums) - 1
    while nums[j] <= nums[i]:
        j -= 1
    nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = reversed(nums[i + 1:])
    return True


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    nums = list(map(int, data))
    next_permutation(nums)
    print(" ".join(map(str, nums)))


if __name__ == "__main__":
    main()
