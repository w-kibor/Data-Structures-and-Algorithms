def move_zeros_to_end(nums):
    """
    Move all zeros to the end of the array while maintaining the order of non-zero elements.
    
    Args:
        nums: List of integers
    
    Returns:
        List with zeros moved to the end
    """
    # Pointer for position to place next non-zero element
    write_pos = 0
    
    # First pass: move all non-zero elements to the front
    for num in nums:
        if num != 0:
            nums[write_pos] = num
            write_pos += 1
    
    # Second pass: fill remaining positions with zeros
    while write_pos < len(nums):
        nums[write_pos] = 0
        write_pos += 1
    
    return nums


# Test
nums = [1, 3, 0, 4, 0, 0, 5]
result = move_zeros_to_end(nums)
print(result)  # Output: [1, 3, 4, 5, 0, 0, 0]