from random import randint
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

class DLL:
    def __init__(self, values = None) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        curr_node = self.head
        while curr_node:
            yield curr_node
            curr_node = curr_node.next

    def __str__(self) -> str:
        values = [str(x.value) for x in self]
        return '->'.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result
    
    def reverse(self):
        curr_node = self.tail
        res = ""
        while curr_node:
            res += str(curr_node.value)
            if curr_node.prev is not None:
                res += "->"
            curr_node = curr_node.prev
        return res

    def add(self, value):
        if not self.head:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = Node(value)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        return self.tail
    
    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self
    
customLL = DLL()
customLL.generate(10, 0, 99)
print (customLL)
print (customLL.reverse())
