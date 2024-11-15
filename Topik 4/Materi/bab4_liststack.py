class Stack:
    def __init__(self):
        self._data = list()
        
    def isEmpty(self):
        return len(self._data) == 0
    
    def __len__(self):
        return len(self._data)
    
    def peek(self):
        if self.isEmpty():
            raise Exception('Stack kosong. Tidak ada data top.')
        else:
            return self._data[-1]
        
    def pop(self):
        if self.isEmpty():
            raise Exception('Stack kosong. Tidak ada data yang dapat di-pop.')
        else:
            return self._data.pop()
        
    def push(self, data):
        self._data.append(data)
    