#find closest to n and divisible by m

def closest_to_n_and_divisible_by_m(n, m):
    if m == 0:
        raise ValueError("m cannot be zero.")
    
    # Calculate the closest number to n that is divisible by m
    closest = round(n / m) * m
    
    return closest
#testing the function
n = 10
m = 3
print(closest_to_n_and_divisible_by_m(n, m))

#Time and Space complexities:
#Time Complexity: O(1) - The function performs a constant number of operations regardless of the input size.
#Space Complexity: O(1) - The function uses a constant amount of space for variables