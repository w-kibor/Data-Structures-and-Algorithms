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