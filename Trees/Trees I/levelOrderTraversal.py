class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        from collections import deque
        q, res = deque(),[]
        q.append(root)
        while q:
            lenn = len(q)
            temp=[]
            for _ in range(lenn):
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(temp)
        return res
