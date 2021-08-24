class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        stack, res = [], []
        curr = root
        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            elif stack:
                node = stack.pop()
                res.append(node.val)
                curr = node.right
            else: return res
