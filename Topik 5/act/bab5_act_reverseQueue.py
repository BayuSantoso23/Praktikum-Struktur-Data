from linkedliststack import Stack

# Fungsi reverse_queue() membalik urutan elemen-elemen dalam
# queue yang diberikan sebagai argument.
def reverseQueue(q):
    # [1] Buat sebuah stack sementara untuk menyimpan elemen-elemen queue yang ditukar 
    stackSementara = Stack()


    # [2] Keluarkan semua elemen dari queue dan masukkan ke dalam stack.
    while not q.isEmpty():
        stackSementara.push(q.dequeue())



    # [3] Keluarkan semua elemen dari stack dan kembalikan ke dalam queue
    while not stackSementara.isEmpty():
        q.enqueue(stackSementara.pop())




