class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = []
        l = n * n + 1
        while l > 1:
            l, r = l - len(res), l
            res = [list(range(l, r))] + list(zip(*res[::-1]))
        return res
