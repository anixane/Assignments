"""
Problem: https://leetcode.com/problems/edit-distance/
"""
class Solution:
    def minDistance(self, strr1: str, strr2: str) -> int:
        if len(strr1)==0 or len(strr2)==0:
            return len(strr1)+len(strr2)
        
        dp = [[float('inf')]*len(strr2+"a") for _ in range(len(strr1+"a"))]
        for i in range(len(strr1)+1):
            dp[i][0]=i
        for j in range(len(strr2)+1):
            dp[0][j]=j
        
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if strr1[i-1]==strr2[j-1]:
                    dp[i][j] = min(dp[i][j],dp[i-1][j-1])
                else:
                    # delete = 1 + dp[i - 1][j]
                    # insert = 1 + dp[i][j - 1]
                    # replace = 1 + dp[i - 1][j - 1]
                    dp[i][j] = 1+min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
