"""
Problem Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def buildTree(arr):
            if not arr: return
            mid = len(arr)//2
            root = TreeNode(arr[mid])
            root.left = buildTree(arr[:mid])
            root.right = buildTree(arr[mid+1:])
            return root
        return buildTree(nums)
