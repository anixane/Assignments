"""
Threaded trees. O(n), O(1)
"""

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        def getpredecessor(root):
            if root is None: return None
            curr = root.left
            while curr:
                curr = curr.right
            return curr
        
        res, curr = [], root
        while curr is not None:
            if curr.left is None:
                res.append(curr.val)
                curr = curr.right
            else:
                predecessor = getpredecessor(curr)
                if predecessor.right is None:
                    predecessor.right = curr
                    curr = curr.left
                else:
                    predecessor.right = None
                    res.append(curr.val)
                    curr = curr.right
        return res
