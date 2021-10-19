"""
Problem: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
Paradigm: Simple application of DFS
"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root,curr_max):
            nonlocal count
            if root is None: return
            if root.val>=curr_max: count+=1
            dfs(root.left,max(root.val,curr_max))
            dfs(root.right,max(root.val,curr_max))
        dfs(root,float('-inf'))
        return count
