class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None: return []
        from collections import deque
        q, res, level = deque(),1, 1
        q.append(root)
        maxx = float('-inf')
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
            if sum(temp)>maxx:
                res=level
                maxx = sum(temp)
            level+=1
        return res
