import ctypes

class Array:
    def __init__(self, size):
        if(size <= 0):
            raise ValueError("Array harus mempunyai ukuran > 0")
        else:
            self._size = size
            Carray = ctypes.py_object * size
            self._isi = Carray()
            self.clear(None)
            
    def __len__(self):
        return self._size
    
    def __getitem__(self, index):
        if ( index < 0 or index >= len(self)):
            raise ValueError('Indeks harus dalam rentang yang valid.')
        else:
            return self._isi[index]
        
    def __setitem__(self, index, nilai):
        if(index < 0 or index >= len(self)):
            raise ValueError('Indeks harus berada dalam rentang yang valid')
        else:
            self._isi[index] = nilai
            
    def clear(self, nilai):
        for i in range(len(self)):
            self._isi[i] = nilai
            
    def __iter__(self):
        return _ArrayIterator(self._isi)
    
class _ArrayIterator:
    def __init__(self, iniArray):
        self._refArray = iniArray
        self._curiIndex = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self ._curiIndex < len(self._refArray):
            entry = self._refArray[self._curiIndex]
            self._curiIndex += 1
            return entry
        else:
            raise StopIteration