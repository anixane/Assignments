"""
Problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
Application of DFS
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def getLCA(root,p,q):
            if root is None: return None
            if root==p or root==q: return root
            left = getLCA(root.left,p,q)
            right = getLCA(root.right,p,q)
            
            if left==None and right==None: return None
            if left is not None and right is not None: return root
            if left is None: return right
            else: return left
            
            
        return getLCA(root,p,q)
