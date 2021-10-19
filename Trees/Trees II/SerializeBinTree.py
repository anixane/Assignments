"""
Problem: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
Paradigm: Good DFS Implementation Problem
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(root):
            nonlocal res
            if root is None:
                res.append('N')
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = data.split(',')
        print(values)
        i = 0
        def dfs():
            nonlocal i
            if values[i]=='N':
                i+=1
                return
            # print(values[i])
            root = TreeNode(int(values[i]))
            i+=1
            # if i==len(values): return root
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()
