# Implementasi ADT SortedLinkedList
class SortedLinkedList:
    # Constructor SortedLinkedList (dimulai dengan linked list kosong)
    def __init__(self):
        self._head = None
        self._size = 0

    # Method length() mengembalikan banyaknya elemen dalam sorted linked list.
    # Method ini diakses menggunakan fungsi len().
    def __len__(self):
        return self._size

    # Method add(data) menambahkan data baru ke sorted linked list.
    def add(self, data):
        newNode = _Node(data)
        if self._head is None or self._head.data >= newNode.data:  # Menambah di depan
            newNode.next = self._head
            self._head = newNode
        else:
            curNode = self._head
            while curNode.next is not None and curNode.next.data < newNode.data:
                curNode = curNode.next
            newNode.next = curNode.next  # Hubungkan dengan node berikutnya
            curNode.next = newNode  # Sisipkan node baru
        self._size += 1

    # Method contains(data) digunakan untuk mencari data dalam sorted linked list.
    def __contains__(self, data):
        curNode = self._head
        while curNode is not None:
            if curNode.data == data:
                return True
            curNode = curNode.next
        return False

    # Method remove() menghapus data dari sorted linked list.
    # Method ini mengembalikan data yang dihapus.
    def remove(self, data):
        curNode = self._head
        prevNode = None
        
        while curNode is not None and curNode.data != data:
            prevNode = curNode
            curNode = curNode.next
        
        if curNode is None:
            raise ValueError('Data tidak ditemukan.')
        
        self._size -= 1
        if prevNode is None:  # Data yang dihapus adalah node pertama
            self._head = curNode.next
        else:
            prevNode.next = curNode.next
        
        return curNode.data

    # Method iterator untuk men-traverse sorted linked list
    def __iter__(self):
        return _LinkedListIterator(self._head)


# Definisikan class _Node sebagai penyimpanan data dan referensi 
# ke node selanjutnya.
class _Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Class iterator untuk ADT Sorted Linked List
class _LinkedListIterator:
    def __init__(self, listHead):
        self._curNode = listHead
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self._curNode is None:
            raise StopIteration
        else:
            data = self._curNode.data
            self._curNode = self._curNode.next
            return data
