#multiplcation table 

def multiplication_table(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f"{i} x {j} = {i*j}", end="\t")
        print()  # New line after each row

#testing the function
multiplication_table(5)

#Time and Space complexities:
#Time Complexity: O(n^2) - The function performs n^2 operations for an n x n multiplication table.
#Space Complexity: O(1) - The function uses a constant amount of space for variables