"""
Leetcode: https://leetcode.com/problems/median-of-two-sorted-arrays/
"""

class Solution:
    def findMedianSortedArrays(self, arr1: List[int], arr2: List[int]) -> float:
        if len(arr1)>len(arr2):
            return self.findMedianSortedArrays(arr2,arr1)
        x,y = len(arr1),len(arr2)
        low, high = 0, x
        
        while low<=high:
            partition_x = (low+high)//2
            partition_y = (x+y+1)//2 - partition_x
            
            left_max_X = arr1[partition_x-1] if partition_x>0 else float('-inf')
            right_min_X = arr1[partition_x] if partition_x<x else float('inf')
            
            left_max_Y = arr2[partition_y-1] if partition_y>0 else float('-inf')
            right_min_Y = arr2[partition_y] if partition_y<y else float('inf')
            
            #check conditions now
            if left_max_X<=right_min_Y and left_max_Y<=right_min_X:
                #partition found condition
                if (x+y)%2==0:
                    return (max(left_max_X,left_max_Y)+min(right_min_X,right_min_Y))/2
                else:
                    return max(left_max_X,left_max_Y)
            elif left_max_X > right_min_Y:
                high = partition_x - 1
            else:
                low = partition_x + 1
