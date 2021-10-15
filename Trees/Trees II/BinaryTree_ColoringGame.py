"""
Problem: https://leetcode.com/problems/binary-tree-coloring-game/
Logic:
That node will definitely be parent ,left or right child of red color,since we need to block one of the sides completely for red color.
Hence we find no of nodes on left subtree,right subtree of red and from root to red color and choose max of them
as our first blue point.Then simply check if its value >n//2.
"""

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def dfs(node):
            if not node:
                return 0
            return dfs(node.left)+dfs(node.right)+1
        head=None
        def traverse(node):
            nonlocal head
            if not node:
                return 
            if node.val==x:
                head=node
                return
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        left=dfs(head.left)
        right=dfs(head.right)
        top=n-left-right-1
        Max=max(left,right,top)
        if Max>n//2:
            return True
        return False
