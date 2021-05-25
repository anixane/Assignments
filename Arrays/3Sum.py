"""
Leetcode: https://leetcode.com/problems/3sum/
Approach:sort the array and use two-pointer technique
"""

class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        if not arr: return None
        mapp = {}
        arr.sort()
        for i in range(len(arr)-2):
            left,right = i+1,len(arr)-1
            while left<right:
                currentSum = arr[left]+arr[right]+arr[i]
                if currentSum==0: 
                    mapp[tuple([arr[i],arr[left],arr[right]])] = True
                    left+=1
                elif currentSum<0: left+=1
                else: right-=1
        return [key for key in mapp]
