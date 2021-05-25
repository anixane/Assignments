"""
Leetcode: https://leetcode.com/problems/two-sum/
Approach:
  1. maintain a mapp to preserve indexes. Keep duplicate values edge case in mind.
  2. sort the array
  3. apply 2-pointer technique
"""

class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        if not arr: return None
        from collections import defaultdict
        mapp = defaultdict(list)
        for i in range(len(arr)):
            mapp[arr[i]].append(i)
            
        def getIndexes(val1,val2):
            nonlocal mapp
            if val1==val2:
                return [mapp[val1][0],mapp[val1][1]]
            return [mapp[val1][0],mapp[val2][0]]
        
        arr.sort()
        low,high = 0,len(arr)-1
        while low<high:
            if arr[low]+arr[high]==target: return getIndexes(arr[low],arr[high])
            if arr[low]+arr[high]<target: low+=1
            else:
                high-=1
