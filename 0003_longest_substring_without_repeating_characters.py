
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = 0
        max_length = 0

        for pts in range(1, len(s)):
            if(s[pts] in s[start:pts]):
                max_length = len(s[start:pts]) if (len(s[start:pts]) > max_length) else max_length
                start = s[start:pts].index(s[pts]) + 1 + start
            else:
                if(pts == len(s) - 1):
                    max_length = max([max_length, len(s[start:])])

        return max_length if(max_length != 0) else len(s)
