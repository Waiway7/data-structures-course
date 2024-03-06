class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def prepend(self, value) -> None:
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def remove(self, index) -> Node:
        if index + 1 > self.length or index < 0:
            return None
        elif index == 0:
            pop_node = self.head
            if (self.length > 1):
                self.head = self.head.next
            else:
                self.head = None
                self.tail = None
            pop_node.next = None
            self.length -= 1
            return pop_node
        else:
            tmp_node = self.head
            for _ in range(index - 1):
                tmp_node = tmp_node.next
            pop_node = tmp_node.next
            
            if pop_node.next == None:
                self.tail = tmp_node
            tmp_node.next = tmp_node.next.next
            pop_node.next = None
            self.length -= 1 

            return pop_node
    def reverse(self):
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head, self.tail = self.tail, self.head
    def find_middle(self):
        slow, fast = self.head, self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        print (slow.value)
        return slow
    def remove_duplicates(self):
        if self.head is None: return None
        curr_node = self.head
        _set = set()
        _set.add(curr_node.value)

        while curr_node.next:
            if curr_node.next.value in _set:
                curr_node.next = curr_node.next.next
                self.length -= 1
            else:
                _set.add(curr_node.next.value)
                curr_node = curr_node.next
        self.tail = curr_node
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
# new_linked_list.append(50)
new_linked_list.find_middle()
print (new_linked_list)