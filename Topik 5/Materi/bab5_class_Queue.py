class Queue:
    def __init__(self):
        self._qlist = list()
        
    def isEmpty(self):
        return len(self) == 0
    
    def __len__(self):
        return len(self._qlist)
    
    def enqueue(self, data):
        self._qlist.append(data)
        
    def dequeue(self):
        if self.isEmpty():
            raise Exception('Queue is empty')
        else:
            return self._qlist.pop(0)
        
        
    
    