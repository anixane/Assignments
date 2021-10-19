"""
Problem: https://leetcode.com/problems/binary-tree-pruning/
"""
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if root is None: return None
            if root.left:
                dfs(root.left)
                if root.left.val!=1 and root.left.left is None and root.left.right is None:
                    root.left = None
            if root.right:
                dfs(root.right)
                if root.right.val!=1 and root.right.left is None and root.right.right is None:
                    root.right = None
            return root
        
        root = dfs(root)
        if root.val !=1 and root.left is None and root.right is None:
            return None
        return root
