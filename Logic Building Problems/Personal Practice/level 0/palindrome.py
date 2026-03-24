class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
       #initialize the pointers
        left=0
        right=len(s)-1
       #loop until the pointers meet
        while left<right:
           if s[left]!=s[right]:
               return False
           left+=1
           right-=1
        return True  

print(Solution().isPalindrome(121))

# using slicing
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        return s==s[::-1] #type: ignore

print(Solution().isPalindrome(121))

#using mathematics logic
#we willuse modulo %10 to find the last digit and //10 to remove the last digit

class Solution:
    def isPalindrome(self, x: int) -> bool:
        #negative numbers are not palindromes
        if x<0:
            return False
        original=x
        reversed_num=0
        while x>0:
            #get the last digit
            last_digit=x%10
            #reverse the number
            reversed_num=reversed_num*10+last_digit
            #remove the last digit
            x=x//10
        #compare the original and reversed number
        return original==reversed_num

