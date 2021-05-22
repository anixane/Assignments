"""
Leetcode: https://leetcode.com/problems/subarray-sum-equals-k/
"""

class Solution:
    def subarraySum(self, nums: List[int], targetSum: int) -> int:
        from collections import defaultdict
        mapp = defaultdict(int)
        sumSoFar, prefixSum = 0, []
        
        #make a prefix array with hashmap insertion
        for num in nums:
            sumSoFar+=num
            prefixSum.append(sumSoFar)
            mapp[sumSoFar]+=1
            
        #main logic for calculating result
        res,diff = 0,0
        for item in prefixSum:
            num = targetSum + diff
            if num in mapp:
                res+=mapp[num]
            diff = item
            mapp[diff]-=1
        return res