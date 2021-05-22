"""
Leetcode: https://leetcode.com/problems/search-in-rotated-sorted-array/

Approach: only best solution is to implement is binary search
Idea: To find the sorted side of array and apply binary search on sorted part.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #only solution is to implement is binary search
        low,high = 0,len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target: return mid
            #we need to check which side is sorted
            if nums[mid]>=nums[low]: #left side is sorted
                if nums[low]<=target<=nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
                    
            else: #right side is sorted
                if nums[mid]<=target<=nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1