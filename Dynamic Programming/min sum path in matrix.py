"""
Problem: https://leetcode.com/problems/minimum-path-sum/
"""

class Solution:
    def minPathSum(self, dp: List[List[int]]) -> int:
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i==0 and j==0: continue
                if i==0:
                    dp[i][j] += dp[i][j-1]
                    continue
                if j==0:
                    dp[i][j] += dp[i-1][j]
                    continue
                dp[i][j] += min(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
