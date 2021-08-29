class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(root1,root2):
            if root1 is None and root2 is None: return True
            if root1 is None or root2 is None: return False
            if root1.val==root2.val:
                return isMirror(root1.left,root2.right) and isMirror(root1.right,root2.left)
            return False
        return isMirror(root,root)
