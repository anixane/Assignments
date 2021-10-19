"""
Problem: https://leetcode.com/problems/balance-a-binary-search-tree/
Paradigm: Simple amalgamation of 2 problem, inorder traversal and build BST from sorted array
"""
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if root is None: return []
            curr, stack, res = root, [], []
            while True:
                if curr:
                    stack.append(curr)
                    curr = curr.left
                elif stack:
                    node = stack.pop()
                    res.append(node.val)
                    curr = node.right
                else: return res
        
        def build(arr):
            if not arr: return
            mid = len(arr)//2
            root = TreeNode(arr[mid])
            root.left = build(arr[:mid])
            root.right = build(arr[mid+1:])
            return root
        
        if root is None: return None
        arr = inorder(root)
        return build(arr)
