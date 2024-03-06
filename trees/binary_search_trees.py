from collections import *
class BSTNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.left is None:
            rootNode.left = BSTNode(nodeValue)
        else:
            insertNode(rootNode.left, nodeValue)
    else:
        if rootNode.right is None:
            rootNode.right = BSTNode(nodeValue)
        else:
            insertNode(rootNode.right, nodeValue)
    return "The node has been sucessfully inserted"

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
    if not root:
        return
    queue = deque([root])
    while queue:
        root = queue.popleft()
        print(root.data)
        if root.left: queue.append(root.left)
        if root.right: queue.append(root.right)

def searchNode(root, val):
    if root:
        if root.data == val:
            return root
        if val < root.data:
            return searchNode(root.left, val)
        else:
            return searchNode(root.right, val)
    else:
        return "value does not exist in the tree!!!!!"
    
def minValue(root):
    current = root
    while (current.left):
        current = current.left
    return current

def deleteNode(root, val):
    if root is None:
        return root
    #replaces the targeted root with the preceding root
    if val < root.data:
        root.left = deleteNode(root.left, val)
    elif val > root.data:
        root.right = deleteNode(root.right, val)
    else:
        #if root has no or only one child then preceding root.left or root.right will be set to none
        if not root.left:
            temp = root.right
            root = None
            return temp
        if not root.right:
            temp = root.left
            root = None
            return temp
        #finds min val of the right subtree and designate that node as the replacement for the deleted node
        #min val of the right subtree is used as it fits the conditions of the binary search subtree
        #the replacement is done via replacing the root data/value with the respective min val of the right subtree
        #finally the min val node of the right subtree will be deleted 
        temp = minValue(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)
    return root

newBST = BSTNode(None)
insertNode(newBST, 70)
# insertNode(newBST, 50)
insertNode(newBST, 90)
# insertNode(newBST, 30)
# insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
# insertNode(newBST, 20)
# insertNode(newBST, 40)

# deleteNode(newBST, 70)
# print (newBST.data)

