"""
Problem: https://www.geeksforgeeks.org/flip-binary-tree/
"""

class TreeNode(object):
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def getLevelOrderTraversal(self,root):
        if root is None: return
        from collections import deque
        q,res = deque([root]),[]
        while q:
            count = len(q)
            currentLevel = []
            for _ in range(count):
                node = q.popleft()
                currentLevel.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(currentLevel)
        for item in res:
            print(item)
        return
    
    def flipTreeUpsideDown(self,root):
        if root is None or root.left is None: return root
        prev,next,lastRight = None,None, None
        curr = root
        while curr:
            next = curr.left
            curr.left = lastRight
            lastRght = curr.right
            curr.right = prev
            prev = curr
            curr = next
        return prev
    
    def createTree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        return root
    

Operation = Solution()
root = Operation.createTree()
Operation.getLevelOrderTraversal(root)
flippedTree = Operation.flipTreeUpsideDown(root)
Operation.getLevelOrderTraversal(flippedTree)
