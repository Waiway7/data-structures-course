'''
create a stack that can push and pop and min
'''

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.minNode = None

    def pop(self):
        if self.head == None:
            return "Unable to pop as there are no elements in the stack!"
        else:
            pop_node = self.head

            if pop_node.val == self.minNode.val: self.minNode = self.minNode.next
            self.head = self.head.next

            return pop_node
    
    def __str__(self) -> str:
        res = ""
        curr = self.head
        while (curr):
            res += str(curr.val)
            if curr.next:
                res += "->"
            curr = curr.next
        return res

    def push(self, val):
        new_node = Node(val)
        if (self.head == None):
            new_min_node = Node(val)
            self.minNode = new_min_node
            self.head = new_node
        else:
            if self.minNode.val >= val:
                new_min_node = Node(val)
                new_min_node.next = self.minNode
                self.minNode = new_min_node
            new_node.next = self.head
            self.head = new_node

    def min(self):
        if (self.head == None):
            return None
        else:
            return self.minNode.val
        
stack = Stack()
stack.push(3)
stack.push(5)
stack.push(7)
stack.push(2)
stack.push(4)
stack.push(1)
print (stack.pop().val)
print (stack.pop().val)
print (stack.pop().val)
print (stack.min())

