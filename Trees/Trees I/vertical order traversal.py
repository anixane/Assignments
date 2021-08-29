class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import defaultdict
        mapp = defaultdict(list)
        def getHorizontalDistance(root,horizontalDistance):
            nonlocal mapp
            if root is None: return
            mapp[horizontalDistance].append(root.val)
            getHorizontalDistance(root.left,horizontalDistance-1)
            getHorizontalDistance(root.right,horizontalDistance+1)
            
        getHorizontalDistance(root,0)
        res = []
        for key in sorted(mapp.keys()):
            res.append(mapp[key])
        return res
