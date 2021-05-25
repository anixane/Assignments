"""
Leetcode: https://leetcode.com/problems/previous-permutation-with-one-swap/
"""

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        isStrictlyDecreasingFlag = True
        n = len(arr)
        for i in range(n-2,-1,-1):
            if arr[i]>arr[i+1]:
                isStrictlyDecreasingFlag = False
                break
        
        if isStrictlyDecreasingFlag: return arr
        
        for j in range(n-1,i,-1):
            if arr[i]>arr[j]:
                currentElement = arr[j]
                # neglect all the adjacent values equal to currentElement
                while arr[j] == currentElement:
                    j-=1
                j+=1
                #swap
                arr[i],arr[j] = arr[j],arr[i]
                break
        return arr
                