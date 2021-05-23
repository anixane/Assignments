"""
Leetcode: https://leetcode.com/problems/product-of-array-except-self/

Approach:
1. maintain prefix and postfix array of multiplication of elements.
2. calculate the result in one pass.
"""

class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        prefix, postfix = [1],[]
        pre_res,post_res = 1,1
        for i in range(0,len(arr)):
            item = arr[i]
            pre_res*=item
            prefix.append(pre_res)
        for i in range(len(arr)-1,-1,-1):
            post_res*=arr[i]
            postfix.append(post_res)
        postfix.reverse()
        postfix.append(1)
        
        res = []
        for i in range(1,len(postfix)):
            res.append(prefix[i-1]*postfix[i])
        return res