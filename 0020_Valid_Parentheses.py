class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True

        char_map, stack={'(':')','{':'}','[':']'},[]
        for l in s:
            if not stack or stack[-1] not in char_map or char_map[stack[-1]] != l:
                stack.append(l)
            else:
                stack.pop()
        return True if not stack else False
