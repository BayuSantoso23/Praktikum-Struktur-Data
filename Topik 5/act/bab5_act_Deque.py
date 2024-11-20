# Implementasi ADT Deque menggunakan list.
class Deque:
    # Constructor unutk membuat deque baru.
    # Field 1: list yang digunakan untuk menyimpan elemen-elemen deque.
    def __init__(self):
        # Tuliskan implementasi constructor di bawah.
        self._kotak = []


    # Method isEmpty() mengembalikan True jika deque kosong dan
    # mengembalikan False jika deque tidak kosong.
    def isEmpty(self):
        # Tuliskan implementasi method isEmpty di bawah.
        return len(self._kotak) == 0
        
        
        
    # Method length() mengembalikan banyaknya elemen dalam deque.
    # Method ini diakses menggunakan fungsi len().
    def __len__(self):
        # Tuliskan implementasi method __len__ di bawah.
        return len(self._kotak)
        


    # Method addFront(data) menambahkan data ke bagian depan dari deque.
    # Method ini tidak mengembalikan nilai.
    def addFront(self, data):
        # Tuliskan implementasi method addFront di bawah.
        self._kotak.insert(0, data)
        
        
        
    # Method addRear(data) menambahkan data ke bagian belakang dari deque.
    # Method ini tidak mengembalikan nilai.
    def addRear(self, data):
        # Tuliskan implementasi method addRear di bawah.
        self._kotak.append(data)



    # Method removeFront() menghapus elemen bagian depan dari deque.
    # Method ini mengembalikan nilai data yang dihapus.
    # Jika method ini dipanggil pada deque kosong, maka method ini meng-raise
    # sebuah eksepsi.
    def removeFront(self):
        # Tuliskan implementasi method removeFront di bawah.
        return self._kotak.pop(0)
        
        
        
    # Method removeRear() menghapus elemen bagian belakang dari deque.
    # Method ini mengembalikan nilai data yang dihapus.
    # Jika method ini dipanggil pada deque kosong, maka method ini meng-raise
    # sebuah eksepsi.
    def removeRear(self):
        # Tuliskan implementasi method removeRear di bawah.
        return self._kotak.pop()
        
        
        
