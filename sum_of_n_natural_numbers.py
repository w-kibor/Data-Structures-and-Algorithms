#sum of n natural numbers

def sum_of_n_natural_numbers(n):
    return n * (n + 1) // 2
#testing the function
print(sum_of_n_natural_numbers(10))

#Time and Space complexities:
#Time Complexity: O(1) - The function performs a constant number of operations regardless of the input size.
#Space Complexity: O(1) - The function uses a constant amount of space for variables