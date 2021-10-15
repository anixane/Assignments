"""
Problem: https://practice.geeksforgeeks.org/problems/clone-a-binary-tree/
"""

class Solution:
    def cloneTree(self, tree):
        from collections import defaultdict
        mapp = defaultdict()
        def clone(root):
            nonlocal mapp
            if root is None: return
            new = Node(root.data)
            mapp[new] = new
            new.left = clone(root.left)
            new.right = clone(root.right)
            if root.random:
                if root.random in mapp:
                    new.random = mapp[root.random]
                else:
                    new.random = Node(root.random.data)
                    mapp[new.random] = new.random
            else:
                new.random = None
            return new
        return clone(tree)
