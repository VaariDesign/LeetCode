class Solution(object):
    def isInterleave(self, s1, s2, s3):

        if len(s3) != len(s1+s2): return False

        dp = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]
        dp[0][0] = True
        for i in range(1, len(s1)+1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] = True
            else:
                break
        for j in range(1, len(s2)+1):
            if s2[j-1] == s3[j-1]:
                dp[0][j] = True
            else:
                break
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if (dp[i-1][j] and s1[i-1] == s3[i-1+j]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1]):
                    dp[i][j] = True
        return dp[-1][-1]
