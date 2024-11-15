from bab2_array1d import Array

class Array2D:
    def __init__(self, bykBaris, bykKolom):
        self._arrBaris = Array(bykBaris)
        
        for i in range(bykBaris):
            self._arrBaris[i] = Array(bykKolom)
            
    def bykBaris(self):
        return len(self._arrBaris)
    
    def bykKolom(self):
        return len(self._arrBaris[0])
    
    def clear(self, nilai):
        for baris in range(self.bykBaris()):
            self._arrBaris[baris].clear(nilai)
            
    def __getitem__(self, indeksTuple):
        if len(indeksTuple) != 2:
            raise IndexError('Indeks tidak valid.')
        else:
            brs = indeksTuple[0]
            klm = indeksTuple[1]
            
            if brs < 0 or brs >= self.bykBaris() \
                or klm < 0 or klm >= self.bykKolom():
                raise IndexError('Indeks tidak valid.')
            else:
                arr1D = self._arrBaris[brs]
                elm = arr1D[klm]
                return elm
            
    def __setitem__(self, indexTuple, nilai):
        if len(indexTuple) != 2:
            raise IndexError('Indeks tidak valid.')
        else:
            brs = indexTuple[0]
            klm = indexTuple[1]
            
            if brs < 0 or brs >= self.bykBaris() \
                or klm < 0 or klm >= self.bykKolom():
                raise IndexError('Indeks tidak valid.')
            else:
                arr1D = self._arrBaris[brs]
                arr1D[klm] = nilai