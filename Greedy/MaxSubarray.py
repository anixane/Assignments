"""
Problem: https://leetcode.com/problems/maximum-subarray/
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Called Kadane's Algorithm
        """
        current_max,maxx = nums[0], nums[0]
        for i in range(1,len(nums)):
            current_max = max(current_max+nums[i],nums[i])
            maxx = max(maxx,current_max)
        return maxx
