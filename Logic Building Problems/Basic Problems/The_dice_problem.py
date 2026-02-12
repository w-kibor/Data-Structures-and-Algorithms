#The dice problem

def dice_problem(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        dp = [0] * (n + 1)
        dp[1], dp[2], dp[3] = 1, 2, 4
        
        for i in range(4, n + 1):  

            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
        return dp[n]    
    
#testing the function
n = 5
print(dice_problem(n))

#Time and Space complexities:
#Time Complexity: O(n) - The function iterates through the range from 4 to n, performing constant-time operations in each iteration.
#Space Complexity: O(n) - The function uses a list of size n+1 to store intermediate results.