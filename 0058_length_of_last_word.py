class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_length = 0
        if (len(s) == 0):
            return word_length
        if len(s) == 1:
            if s == " ":
                return word_length
            else:
                return 1
        
        for i in reversed(s):
            if i ==" ":
                if word_length != 0:
                    return word_length
            else:
                word_length += 1
        return word_length
