"""
Problem: https://leetcode.com/problems/binary-tree-right-side-view/
"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def getRightView(root):
            if root is None: return []
            from collections import deque
            q, res = deque([root]), []
            while q:
                count, level = len(q),[]
                for _ in range(count):
                    node = q.popleft()
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                res.append(level[-1])
            return res
        return getRightView(root)
                
