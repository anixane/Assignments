"""
Problem: https://www.techiedelight.com/boundary-traversal-binary-tree/
Paradigm: Application of DFS and inorder traversal
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
res = []
def isLeafNode(root):
    return root.left is None and root.right is None

def getLeftBoundary(root):
    if root is None or isLeafNode(root): return
    res.append(root.data)
    if root.left:
        return getLeftBoundary(root.left)
    return getLeftBoundary(root.right)

right = []
def getRightBoundary(root):
    #it should be bottom up so reverse the list with following approach while appending in final result
    if root is None or isLeafNode(root): return
    right.append(root.data)
    if root.right:
        return getRightBoundary(root.right)
    return getRightBoundary(root.left)

def getLeafNodes(root):
    #it should be inorder traversal
    if root is None: return
    getLeafNodes(root.left)
    if isLeafNode(root): res.append(root.data)
    getLeafNodes(root.right)

def getBoundaryTraversal(root):
    if root is None: return
    res.append(root.data)
    getLeftBoundary(root.left)
    getLeafNodes(root)
    getRightBoundary(root.right)
    for item in reversed(right): res.append(item)
    return res

def createTree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.right = Node(10)
    root.right.right.left = Node(11)
    root.left.left.right.left = Node(12)
    root.left.left.right.right = Node(13)
    root.right.right.left.left = Node(14)
    return root

root = createTree()
print(getBoundaryTraversal(root))
