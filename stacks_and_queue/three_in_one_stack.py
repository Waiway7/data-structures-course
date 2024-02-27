

class MultiStack:
    def __init__(self, stacksize) -> None:
        '''
        to create three stacks in one array we simply multiple 3 by the given stack size
        stacksize = 3 muliple stacksize to numberstacks which is 3 and we have an array size of 9
        to keep track of each stack in the array in this case there is a maximum of 3 size per stack 
        the self.sizes will contain the current amount of elements in each stack
        '''
        self.numberstacks = 3
        self.custList = [0] * (stacksize * self.numberstacks)
        self.sizes = [0] * self.numberstacks
        self.stacksize = stacksize

    def isFull(self, stacknum):
        if self.sizes[stacknum] == self.stacksize:
            return True
        else:
            return False
        
    def isEmpty(self, stacknum):
        if self.sizes[stacknum] == 0:
            return True
        else:
            return False
    
    def indexOfTop(self, stacknum):
        '''
        offset will determine the index at x stacknum to be located in the array
        by adding the size of that stacknum and subtracting by 1, that will be the top element in the stacknum
        '''
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1
    
    def push(self, item, stacknum):
        if self.isFull(stacknum):
            return "The stack is full"
        else:
            self.sizes[stacknum] += 1
            self.custList[self.indexOfTop(stacknum)] = item
    
    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            return "The stack is empty"
        else:
            value = self.custList[self.indexOfTop(stacknum)]
            self.sizes[stacknum] -= 1
            return value
    
    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            return "The stack is empty"
        else:
            value = self.custList[self.indexOfTop(stacknum)]
            return value
        
customStack = MultiStack(6)
print (customStack.isFull(0))
print (customStack.isEmpty(1))
customStack.push(1,0)
customStack.push(2,0)
customStack.push(3,0)
print (customStack.pop(0))
print (customStack.peek(0))
customStack.push(4,0)
print (customStack.custList)

class MultiStack:
    def __init__(self, stacksize) -> None:
        self.num_of_stacks = 3
        self.stack = [0] * (stacksize * self.num_of_stacks)
        self.sizes = [0] * self.num_of_stacks
        self.stacksize = stacksize
    
    def isFull(self, stacknum):
        if self.sizes[stacknum] == self.stacksize:
            return True
        else:
            return False
        
    def isEmpty(self, stacknum):
        if self.sizes[stacknum] == 0:
            return True
        else:
            return False
        
    def indexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1
    
    def push(self, val, stacknum):
        if self.isFull(stacknum):
            return "Unable to add to the stack as it is currently full"
        else:
            self.sizes[stacknum] += 1
            self.stack[self.indexOfTop(stacknum)] = val

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            return "Unable to pop as there is no element in the stack."
        else:
            val = self.stack[self.indexOfTop(stacknum)]
            self.sizes[stacknum] -= 1
            return val
        
    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            return "Unable to peek as there is no element in the stack."
        else:
            val = self.stack[self.indexOfTop(stacknum)]
            return val
        
customStack = MultiStack(6)
print (customStack.isFull(0))
print (customStack.isEmpty(1))
customStack.push(1,0)
customStack.push(2,0)
customStack.push(3,0)
print (customStack.pop(0))
print (customStack.peek(0))
customStack.push(4,0)
print (customStack.stack)