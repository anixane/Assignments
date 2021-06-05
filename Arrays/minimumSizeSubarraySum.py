"""
Leetcode: https://leetcode.com/problems/minimum-size-subarray-sum/submissions/
Approach: simple 2 pointer approach with storing the minimum length so far
"""

class Solution:
    def minSubArrayLen(self, target: int, arr: List[int]) -> int:
        if not arr: return 0
        if sum(arr)<target: return 0
        left,right,res = 0,0, float('inf')
        summ = arr[left]
        while left<len(arr) and right<len(arr):
            if summ<target:
                right+=1
                if right<len(arr):
                    summ+=arr[right]
            else:
                res = min(res,right-left+1)
                summ-=arr[left]
                left+=1
        return res
