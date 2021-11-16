"""
Problem: https://leetcode.com/problems/longest-common-subsequence/
"""
class Solution:
    def longestCommonSubsequence(self, strr1: str, strr2: str) -> int:
        dp = [[0]*len(strr2+"a") for _ in range(len(strr1+"a"))]
        for i in range(len(strr1)+1):
            dp[i][0] = 0
        for j in range(len(strr2)+1):
            dp[0][j] = 0
        for i in range(1,len(strr1)+1):
            for j in range(1,len(strr2)+1):
                if strr1[i-1]==strr2[j-1]: #its strr1[i] and strr2[j] in real
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
