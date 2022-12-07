class Solution:
    def reverse(self, x: int) -> int:
        ans = int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])
        return ans if -2**31 <= ans <= 2**31 - 1 else 0
