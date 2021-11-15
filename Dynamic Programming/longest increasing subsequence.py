"""
Problem: https://leetcode.com/problems/longest-increasing-subsequence/
"""
class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        if len(arr)<1:
            return 0
        dp = [1]*len(arr)
        for i in range(len(arr)):
            max_so_far = float('-inf')
            for j in range(i):
                if arr[j]<arr[i]: #main condition
                    max_so_far = max(max_so_far,dp[j]+1)
            dp[i]=max(max_so_far,dp[i])
        return max(dp)
