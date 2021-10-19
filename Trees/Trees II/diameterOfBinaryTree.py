"""
Problem: https://leetcode.com/problems/diameter-of-binary-tree/
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getDia(root):
            if root is None: return 0
            normalDia = height(root.left)+height(root.right)
            leftSubtreeDia = getDia(root.left)
            rightSubtreeDia = getDia(root.right)
            return max(normalDia, leftSubtreeDia, rightSubtreeDia)
        
        def height(root):
            if root is None: return 0
            left = height(root.left)
            right = height(root.right)
            return max(left,right)+1
        
        return getDia(root)
