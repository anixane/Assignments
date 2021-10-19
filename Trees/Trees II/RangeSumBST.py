"""
Problem: https://leetcode.com/problems/range-sum-of-bst/
"""

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        def getSum(root,low,high):
            nonlocal res
            if root is None: return
            if low<=root.val<=high:
                res+=root.val
            getSum(root.left,low,high)
            getSum(root.right,low,high)
        
        getSum(root,low,high)
        return res
