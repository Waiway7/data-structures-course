from binary_trees import LinkedListBinaryTree
from collections import deque

class Traversal():
    def __init__(self):
        self.preorder_arr = []
        self.inorder_arr = []
        self.postorder_arr = []
        self.inorder_arr = []

    def preorder(self, root):
        if not root:
            return
        self.preorder_arr.append(root.data)
        self.preorder(root.left)
        self.preorder(root.right)
    
    def inorder(self, root):
        if not root:
            return
        self.preorder(root.left)
        self.inorder_arr.append(root.data)
        self.preorder(root.right)

    def postorder(self, root):
        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        self.postorder_arr.append(root.data)

    def levelorder(self, root):
        queue = deque([root])
        while queue:
            parent = queue.popleft()
            for child in parent:

    