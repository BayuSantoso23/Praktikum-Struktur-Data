class Stack:
    def __init__(self):
        self._top = None
        self._size = 0
        
    def isEmpty(self):
        return self._top is None
    
    def __len__(self):
        return self._size
    
    def peek(self):
        if self.isEmpty():
            raise Exception('Stack kosong. Tidak ada data top.')
        else:
            return self._top.data
        
    def pop(self):
        if self.isEmpty():
            raise Exception('Stack kosong. Tidak ada data yang dapat di-pop')
        else:
            dataDihapus = self._top.data
            self._top = self._top.next
            self._size -= 1
            return dataDihapus
   
    def push(self, data):
        newNode = _StackNode(data)
        newNode.next = self._top
        self._top = newNode
        self._size += 1
    
   
   
class _StackNode():
    def __init__(self, data):
        self.data = data
        self.next = None
            