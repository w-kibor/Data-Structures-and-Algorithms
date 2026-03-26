class Solution:
    def toLowerCase(self, s: str) -> bool:
        s1= s.join(filter(str.isalnum, s))
        s2=s1.casefold()
        return s2
        