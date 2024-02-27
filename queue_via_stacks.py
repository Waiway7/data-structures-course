'''
use two stacks to implementa queue
'''

class Stack():
    def __init__(self):
        self.stack = []

    def __str__(self) -> str:
        return str(self.stack)
    
    def push(self, ele):
        self.stack.append(ele)

    def pop(self):
        return self.stack.pop()

class QueueviaStack():
    def __init__(self) -> None:
        self.in_stack = Stack()
        self.out_stack = Stack()
    
    def enqueue(self, item):
        self.in_stack.push(item)
    
    def dequeue(self):
        while (len(self.in_stack.stack)):
            self.out_stack.push(self.in_stack.pop())
        res = self.out_stack.pop()
        while (len(self.out_stack.stack)):
            self.in_stack.push(self.out_stack.pop())
        return res
    
queue = QueueviaStack()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print (queue.dequeue())
print (queue.dequeue())
print (queue)
