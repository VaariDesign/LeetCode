class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        
        ans = int(str(x)[::-1])
        
        if ans == x:
            return True
        return False
