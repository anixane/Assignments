class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def getInorder(root):
            if root is None: return []
            stack, res, curr = [],[], root
            while True:
                if curr:
                    stack.append(curr)
                    curr = curr.left
                elif stack:
                    node=stack.pop()
                    res.append(node.val)
                    curr=node.right
                else: return res
        
        inorder = getInorder(root)
        #just check whether it is completely sorted (with unique values) in O(n)
        for i in range(1,len(inorder)):
            if inorder[i-1]>=inorder[i]: return False
        return True
