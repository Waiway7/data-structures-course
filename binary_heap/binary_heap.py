
class BinaryHeap:
    def __init__(self, size) -> None:
        self.heap = (size + 1) * [None]
        self.heap_size = 0
        self.max_size = size + 1
    def peek(self):
        if self.heap_size == 0:
            return None
        return self.heap[1]
    def heapifyTreeInsert(self, index, heapType):
        parentIndex = int(index / 2)
        if index <= 1:
            return 
        if heapType == "Min":
            if self.heap[index] < self.heap[parentIndex]:
                temp = self.heap[index]
                self.heap[index] = self.heap[parentIndex]
                self.heap[parentIndex] = temp
            self.heapifyTreeInsert(parentIndex, heapType)
        elif heapType == "Max":
            if self.heap[index] > self.heap[parentIndex]:
                temp = self.heap[index]
                self.heap[index] = self.heap[parentIndex]
                self.heap[parentIndex] = temp
            self.heapifyTreeInsert(parentIndex, heapType)
    def insertNode(self, val, heapType):
        if self.heap_size + 1 == self.max_size:
            return "The binary heap is full"
        self.heap[self.heap_size + 1] = val
        self.heap_size += 1
        self.heapifyTreeInsert(self.heap_size, heapType)
        return "The value inserted."
    
    def heapifyTreeExtract(self, index, heapType):
        left_index = index * 2
        right_index = index * 2 + 1
        swap_child = 0
        if self.heap_size < left_index:
            return
        elif self.heap_size == left_index:
            if heapType == "Min":
                if self.heap[index] > self.heap[left_index]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[left_index]
                    self.heap[left_index] = temp
                    return
            else:
                if self.heap[index] < self.heap[left_index]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[left_index]
                    self.heap[left_index] = temp
                    return
        else:
            if heapType == "Min":
                if self.heap[left_index] < self.heap[right_index]:
                    swap_child = left_index
                else:
                    swap_child = right_index
                if self.heap[index] > self.heap[swap_child]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[swap_child]
                    self.heap[swap_child] = temp
            else: 
                if self.heap[left_index] > self.heap[right_index]:
                    swap_child = left_index
                else:
                    swap_child = right_index
                if self.heap[index] < self.heap[swap_child]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[swap_child]
                    self.heap[swap_child] = temp
        self.heapifyTreeExtract(swap_child, heapType)
    def extractNode(self, heapType):
        if self.heap_size == 0:
            return None
        else:
            extracted = self.heap[1]
            self.heap[1] = self.heap[self.heap_size]
            self.heap[self.heap_size] = None
            self.heap_size -= 1
            self.heapifyTreeExtract(1, heapType)
            return extracted
        
    def levelOrder(self):
        lvls = []
        def helper(idx, lvl):
            if idx > self.heap_size:
                return
            if len(lvls) == lvl:
                lvls.append([])
            lvls[lvl].append(self.heap[idx])
            helper(idx * 2, lvl + 1)
            helper(idx * 2 + 1, lvl + 1)
        helper(1, 0)
        return lvls
    def deleteHeap(self):
        self.heap = None
        
heap = BinaryHeap(5)
heaptype = "Max"
heap.insertNode(10, heaptype)
heap.insertNode(12, heaptype)
heap.insertNode(14, heaptype)
heap.insertNode(1, heaptype)
print (heap.extractNode(heaptype))
print (heap.levelOrder())
