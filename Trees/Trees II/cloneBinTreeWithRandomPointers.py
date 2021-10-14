"""
Problem: https://practice.geeksforgeeks.org/problems/clone-a-binary-tree/
"""

class Solution:
    def cloneTree(self, root):
        def updateRandomPointers(root, dict):
            # base case
            if dict.get(root) is None:
                return
         
            # update the random pointer of the cloned node
            dict.get(root).random = dict.get(root.random)
         
            # recur for the left and right subtree
            updateRandomPointers(root.left, dict)
            updateRandomPointers(root.right, dict)
            
        def cloneLeftRightPointers(root, dict):
            if root is None:
                return None
         
            # clone all fields of the root node except the random pointer
         
            # create a new node with the same data as the root node
            dict[root] = Node(root.data)
         
            # clone the left and right subtree
            dict[root].left = cloneLeftRightPointers(root.left, dict)
            dict[root].right = cloneLeftRightPointers(root.right, dict)
         
            # return cloned root node
            return dict[root]
            
        def cloneSpecialBinaryTree(root):
            # create a dictionary to store mappings from a node to its clone
            dict = {}
         
            # clone data, left, and right children for each node of the original
            # binary tree, and put references into the dictionary
            cloneLeftRightPointers(root, dict)
         
            # update random pointers from the original binary tree in the dictionary
            updateRandomPointers(root, dict)
         
            # return the cloned root node
            return dict[root]
        
        return cloneSpecialBinaryTree(root)
