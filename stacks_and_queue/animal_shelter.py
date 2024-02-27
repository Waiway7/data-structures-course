class Node:
    def __init__(self, name, animal) -> None:
        self.name = name
        self.animal = animal
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, name, animal):
        animal_node = Node(name, animal)
        if (self.head == None): 
            self.head = self.tail = animal_node
        else:
            self.tail.next = animal_node
            self.tail = self.tail.next

    def isEmpty(self):
        return True if self.head == None else False
    
    def pop(self):
        if self.head == None:
            return None
        else:
            pop_node = self.head
            self.head = self.head.next
            pop_node.next = None
            return pop_node
    
    def pop_specific_animal(self, animal):
        if self.head == None:
            return None
        else:
            curr = self.head
            prev = None
            while curr:
                if curr.animal == animal:
                    prev.next = curr.next
                    return curr
                
                prev = curr
                curr = curr.next
            return None
        
class AnimalShelter():
    def __init__(self):
        self.linked_list_dog_cat = LinkedList()

    def __str__(self) -> str:
        res = ''
        curr = self.linked_list_dog_cat.head
        while (curr):
            res += str(curr.name)
            if curr.next:
                res += "->"
            curr = curr.next
        return res 
    
    def enqueue(self, name, animal):
        self.linked_list_dog_cat.append(name, animal)
    
    def dequeueAny(self):
        if self.linked_list_dog_cat.isEmpty():
            return None
        else:
            return self.linked_list_dog_cat.pop()
        
    def dequeueCat(self):
        if self.linked_list_dog_cat.isEmpty():
            return None
        else:
            if self.linked_list_dog_cat.head.animal == 'Cat':
                return self.linked_list_dog_cat.pop()
            else:
                return self.linked_list_dog_cat.pop_specific_animal('Cat')
    
    def dequeueDog(self):
        if self.linked_list_dog_cat.isEmpty():
            return None
        else:
            if self.linked_list_dog_cat.head.animal == 'Dog':
                return self.linked_list_dog_cat.pop()
            else:
                return self.linked_list_dog_cat.pop_specific_animal('Dog')
            
customQueue = AnimalShelter()
customQueue.enqueue('Cat1', "Cat")
customQueue.enqueue('Cat2', "Cat")
customQueue.enqueue('Dog1', "Dog")
customQueue.enqueue('Cat3', "Cat")
customQueue.enqueue('Dog2', "Dog")
print (customQueue)
customQueue.dequeueCat()
customQueue.dequeueCat()
customQueue.dequeueAny()
print (customQueue)
