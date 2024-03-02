from collections import deque

class AVLNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def preorder(root):
    if not root:
        return
    print (root.data)
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print (root.data)
    inorder(root.right)

def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print (root.data)

def levelorder(root):
    lvls = []
    def helper(root, lvl):
        if not root:
            return
        if lvl == len(lvls):
            lvls.append([])
        lvls[lvl].append(root.data)
        helper(root.left, lvl + 1)
        helper(root.right, lvl + 1)

    helper(root, 0)
    return lvls

def getHeight(root):
    if not root:
        return 0
    return root.height

def rightRotate(node):
    newRoot = node.left
    node.left = newRoot.right
    newRoot.right = node
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    newRoot.height = 1 + max(getHeight(newRoot.left), getHeight(newRoot.right))
    return newRoot

def leftRotate(node):
    newRoot = node.right
    node.right = newRoot.left
    newRoot.left = node
    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    newRoot.height = 1 + max(getHeight(newRoot.left), getHeight(newRoot.right))
    return newRoot

def getBalance(root):
    if not root:
        return 0
    return getHeight(root.left) - getHeight(root.right)

def insertNode(root, val):
    if not root:
        return AVLNode(val)
    elif val < root.data:
        root.left = insertNode(root.left, val)
    else:
        # print (val)
        root.right = insertNode(root.right, val)
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    balance = getBalance(root)
    if balance > 1 and val < root.left.data:
        return rightRotate(root)
    if balance > 1 and val > root.left.data:
        root.left = leftRotate(root.left)
        return rightRotate(root)
    if balance < -1 and val > root.right.data:
        return leftRotate(root)
    if balance < -1 and val < root.right.data:
        root.right = rightRotate(root.right)
        return leftRotate(root)
    return root

def getMinValueNode(root):
    if not root or not root.left:
        return root
    return getMinValueNode(root.left)

def deleteNode(root, val):
    if not root:
        return root
    elif val < root.data:
        root.left = deleteNode(root.left, val)
    elif val > root.data:
        root.right = deleteNode(root.right, val)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.right
            root = None
            return temp
        temp = getMinValueNode(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)
    balance = getBalance(root)
    if balance > 1 and getBalance(root.left) >= 0:
        return rightRotate(root)
    if balance < -1 and getBalance(root.right) <= 0:
        return leftRotate(root)
    if balance > 1 and getBalance(root.left) < 0:
        root.left = leftRotate(root.left)
        return rightRotate(root)
    if balance < -1 and getBalance(root.right) >0:
        root.right = rightRotate(root.right)
        return leftRotate(root)
    return root


newAVL = start = AVLNode(5)
newAVL = insertNode(newAVL, 10)
newAVL = second = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
newAVL = deleteNode(newAVL, 15)
print (levelorder(newAVL))


