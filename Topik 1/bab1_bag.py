class Bag:
    def __init__(self):  # Gunakan __init__ bukan _init_
        self._isi = list()
        
    def __len__(self):  # Gunakan __len__ bukan _len_
        return len(self._isi)
    
    def __contains__(self, nilai):  # Gunakan __contains__ bukan _contains_
        return nilai in self._isi
    
    def add(self, nilai):
        self._isi.append(nilai)
    
    def remove(self, nilai):
        if nilai not in self._isi:
            raise ValueError('Nilai tidak ada dalam bag.')
        else:
            indeks = self._isi.index(nilai)
            return self._isi.pop(indeks)
        
    # Praktikumnya
    def numOf(self, data):
        count = 0
        for item in self._isi:
            if item == data:
                count += 1
        return count
    
    def __iter__(self):  # Gunakan __iter__ bukan _iter_
        return _BagIterator(self._isi)
    
class _BagIterator:
    def __init__(self, isi):  # Gunakan __init__ bukan _init_
        self._isiBag = isi
        self._curIndeks = 0
        
    def __iter__(self):  # Gunakan __iter__ bukan _iter_
        return self
    
    def __next__(self):  # Gunakan __next__ bukan _next_
        if self._curIndeks < len(self._isiBag):
            item = self._isiBag[self._curIndeks]
            self._curIndeks += 1
            return item
        else:
            raise StopIteration
