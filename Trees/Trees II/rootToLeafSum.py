"""
Problem: https://leetcode.com/problems/sum-root-to-leaf-numbers/
Paradigm: Simple application of Brute Force
"""

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        from collections import defaultdict
        mapp = []
        def getNums(root,curr):
            nonlocal mapp
            if root is None: return
            if root.left is None and root.right is None:
                mapp.append(str(curr)+str(root.val))
                return
            getNums(root.left,str(curr)+str(root.val))
            getNums(root.right,str(curr)+str(root.val))
        getNums(root,"")
        res = 0
        for item in mapp:
            res+=int(item)
        return res
