"""
Problem: https://leetcode.com/problems/house-robber/
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Constraints:
            1. If you wana rob current house (i), you can't rob the previous house (i-1) and next house (i+1). You can rob house(i-2).
            2. If you don't wana rob the current house(i), you can rob the previous house (i-1) and next house (i+1).
        """
        # Trying Top-Down Approach, got TLE
        
        arr = nums
        def getMaxAmount(n):
            nonlocal arr
            if n==0: return arr[0]
            if n==1: return max(arr[0],arr[1])
            if n<0: return 0
            return max(getMaxAmount(n-1),getMaxAmount(n-2)+arr[n])
        return getMaxAmount(len(arr)-1)
        
    
        # Trying Top-Down Approach with memoization, really fast
        
        from collections import defaultdict
        mapp = defaultdict(int)
        arr = nums
        if len(arr)>1:
            mapp[0], mapp[1] = arr[0], max(arr[0],arr[1])
            def getMaxAmount(n):
                nonlocal arr
                if n<0: return 0
                if n in mapp: return mapp[n]
                res = max(getMaxAmount(n-1),getMaxAmount(n-2)+arr[n])
                mapp[n] = res
                return mapp[n]
            return getMaxAmount(len(arr)-1)
        return max(arr)
        
    
        #Trying Tabulation method (bottom-up), took same time as memoization.
        if len(nums)>1:
            dp = [0 for _ in range(len(nums))]
            dp[0],dp[1] = nums[0],max(nums[0],nums[1])
            for i in range(2,len(nums)):
                dp[i] = max(dp[i-1],dp[i-2]+nums[i])
            return dp[-1]
        return max(nums)
