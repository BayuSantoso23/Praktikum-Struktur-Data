from bab3_linkedlist import LinkedList

def main():
    
    myList = LinkedList()

    myList.addFirst(34)
    myList.addFirst(45)
    myList.addFirst(22)
    myList.addFirst(21)
    myList.addFirst(90)

    # Mencari Nilai dalam Linked List
    nilai = int(input('Masukkan nilai yang dicari: '))
    if nilai in myList:
        print(f'{nilai} ditemukan dalam linked list.')
    else:
        print(f'{nilai} tidak ditemukan dalam linked list.')   
        
    # Menghapus Data yang ada dalam Linked List
    nilai = int(input('Masukkan nilai yang dihapus: '))
    try:
        myList.remove(nilai)
        print(f'{nilai} dihapus dari linked list.')
    except ValueError:
        print('Data tidak ditemukan. Tidak ada data yang di-remove')
        
    # Menampilkan keseluruhan data
    for data in myList:
        print(data)

main()