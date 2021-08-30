class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def getMin(root):
            if root is None: return inf
            if root.left is None and root.right is None: return 1
            return min(getMin(root.left),getMin(root.right))+1
        if root is None: return 0
        return getMin(root)
