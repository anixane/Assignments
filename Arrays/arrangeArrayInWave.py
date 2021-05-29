"""
GFG: https://www.geeksforgeeks.org/sort-array-wave-form-2/
Approach 1: sort and swap alternate elements
Approach 2: focus on retaining the order of wave throughout (wiggle sort algo variation)
"""

def getWavedArray(nums):
    i = 0
    while i < len(nums) - 1:
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        i += 1
        if i == len(nums) - 1:
            break
        if nums[i] < nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        i += 1
