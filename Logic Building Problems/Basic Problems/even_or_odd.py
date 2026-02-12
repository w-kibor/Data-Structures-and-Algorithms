#checking if a number is even or odd

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

#testing the function
print(even_or_odd(112345678)) 

#Time and Space complexities:
#Time Complexity: O(1) - The function performs a constant number of operations regardless of the input size.
#Space Complexity: O(1) - The function uses a constant amount of space for variables