class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0
        
    def isEmpty(self):
        return self._head is None
    
    def __len__(self):
        return self._count
    
    def enqueue(self,data):
        newNode = _QueueNode(data)
        if self.isEmpty():
            self._head = newNode
        else:
            self._tail.next = newNode
        self._tail = newNode
        self._count += 1
        
    def dequeue(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        else:
            node = self._head
            self._head = self._head.next
            self._count -= 1
            return node.data

class _QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    