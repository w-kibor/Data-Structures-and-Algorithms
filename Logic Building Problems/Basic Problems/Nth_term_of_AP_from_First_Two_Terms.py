#Nth term of AP from first two terms

def nth_term_of_ap(a1, a2, n):
    if n < 1:
        raise ValueError("n must be a positive integer.")
    
    d = a2 - a1  # common difference
    nth_term = a1 + (n - 1) * d
    return nth_term

#testing the function
a1 = 2
a2 = 5
n = 4
print(nth_term_of_ap(a1, a2, n))

#Time and Space complexities:
#Time Complexity: O(1) - The function performs a constant number of operations regardless of the input size.
#Space Complexity: O(1) - The function uses a constant amount of space for variables