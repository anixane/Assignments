"""
Problem: https://www.codingninjas.com/codestudio/problem-details/lowest-common-ancestor-of-a-binary-tree-iii_1280134
Idea: Its simple "finding intersection of 2 linked lists" implementation
"""
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

def lowestCommonAncestor(n1, n2):
	from collections import defaultdict
    mapp = defaultdict()
    curr = n1
    while curr:
        mapp[curr]=True
        curr = curr.parent
    curr = n2
    while curr:
        if curr in mapp:
            return curr
        curr = curr.parent
    return None
