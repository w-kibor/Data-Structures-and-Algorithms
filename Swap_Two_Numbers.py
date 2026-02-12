#swapping two numbers

def swap(a, b):
    a, b = b, a
    return a, b

#testing the function
a, b = 5, 10
a, b = swap(a, b)
print(a, b)

#Time and Space complexities:
#Time Complexity: O(1) - The function performs a constant number of operations regardless of the input size.
#Space Complexity: O(1) - The function uses a constant amount of space for variables