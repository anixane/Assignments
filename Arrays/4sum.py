"""
Leetcode: https://leetcode.com/problems/4sum/
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #trying with n-square solution
        def bruteForceWithTwoPointers(arr,target):
            if not arr: return []
            arr.sort()
            res = []
            for i in range(len(arr)):
                for j in range(i+1,len(arr)):
                    k = j+1
                    l = len(arr)-1
                    while k<l:
                        if arr[i]+arr[j]+arr[k]+arr[l]>target:
                            l-=1
                        elif arr[i]+arr[j]+arr[k]+arr[l]<target:
                            k+=1
                        else:
                            #when we get a match
                            currentResult = [arr[i],arr[j],arr[k],arr[l]]
                            currentResult.sort()
                            if currentResult not in res:
                                res.append(currentResult)
                            k+=1
                            l-=1
            return res
        # return bruteForceWithTwoPointers(nums,target)
        
        def approachUsingHash(arr,target):
            if not arr: return []
            arr.sort()
            res = []
            for i in range(len(arr)):
                for j in range(i+1,len(arr)):
                    prev = set()
                    for k in range(j+1, len(arr)):
                        temp = target - arr[i] - arr[j] - arr[k]
                        if temp in prev:
                            val = [arr[i], arr[j], temp, arr[k]]
                            val.sort()
                            if val not in res:
                                res.append(val)
                        prev.add(arr[k])
            return res
        
        # return approachUsingHash(nums,target)
        
        def approachUsingHashAndSet(arr,target):
            nums.sort()
            prev = dict()
            result = set()
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i] + nums[j] in prev.keys():
                        prev[nums[i] + nums[j]].append((i, j))
                    else:
                        prev[nums[i] + nums[j]] = [(i, j)]

            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if target - nums[i] - nums[j] in prev.keys():
                        for pair in prev[target - nums[i] - nums[j]]:
                            if pair[1] < i:
                                result.add((nums[pair[0]], nums[pair[1]], nums[i], nums[j]))

            return [list(item) for item in result]
        
        return approachUsingHashAndSet(nums,target)
