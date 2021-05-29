"""
Leetcode: https://leetcode.com/problems/find-pivot-index/
Approach 1: maintain prefix sum and suffix sum array, return the index where prefixsumm == postfixsumm, will take some extra space
Approach 2: maintain running sum and compare in each iteration. No extra space.
"""

def getEquilibriumOfArray(arr):
    leftsum, summ = 0, sum(arr)
    for i in range(len(arr)):
        summ = summ-arr[i]
        if summ==leftsum: return i
        leftsum+=arr[i]
    return -1
