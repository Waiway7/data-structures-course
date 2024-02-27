'''
create a stack that at x size ti will create a new stack
'''

class Stack:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.stack = []

    def __str__(self):
        return str(self.stack)
    
    def push(self, ele):
        if (len(self.stack) > 0 and len(self.stack[-1]) < self.capacity):
            self.stack[-1].append(ele)
        else:
            self.stack.append([ele])
    def pop(self):
        if (len(self.stack) > 0):
            n = len(self.stack) - 1
            while n >= 0:
                if len(self.stack[n]) > 0:
                    return self.stack[n].pop()
                n -= 1
        else:
            return None
    def pop_at(self, stacknum):
        if stacknum <= len(self.stack):
            if len(self.stack[stacknum - 1]) == 0:
                return None
            else:
                return self.stack[stacknum - 1].pop()
        else:
            return None
plates = Stack(3)
plates.push(1)
plates.push(2)
plates.push(3)
plates.push(4)
plates.push(5)
plates.push(6)
plates.push(7)
plates.push(8)
print (plates.pop_at(1))
print (plates.pop_at(3))
print (plates.push(8))
print (plates.push(3))
print (plates)