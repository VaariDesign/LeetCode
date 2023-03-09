class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = []
        dp.append([""])

        for i in range(1, n + 1):
            solutions = []
            for j in range(i):
                solutions.extend(["(" + l + ")" + r for l in dp[j] for r in dp[i - 1 - j]])
            dp.append(solutions)  
            
        return dp[n]
