from bab5_class_linkedListQueue import Queue

def main():
    cobaQueue = Queue()
    
    if cobaQueue.isEmpty():
        print("Queue Kosong")
    else:
        print("Queue tidak kosong. Isi : ", len(cobaQueue))
        
    input_data = 'Masukkan nilai integer (nilai negatif untuk mengakhiri): '
    
    nilai = int(input(input_data))
    
    while nilai > 0:
        cobaQueue.enqueue(nilai)
        nilai = int(input(input_data))
            
    print('Panjang queue: ', end='')
    print(len(cobaQueue))
    print()
    
    print('Isi Queue')
    for i in range(0, len(cobaQueue)-3):
        nilai = cobaQueue.dequeue()
        if len(cobaQueue) > 3:
            print(nilai, end=' ')
        else:
            print(nilai)
            
    if cobaQueue.isEmpty():
        print('Queue Kosong')
    else:
        print('Queue tidak kosong. Isi: ', len(cobaQueue))      
        
    print()
    print('Sisa isi queue: ')
    while not cobaQueue.isEmpty():
        nilai = cobaQueue.dequeue()
        if not cobaQueue.isEmpty():
            print(nilai, end=' ')
        else:
            print(nilai)
            
    if cobaQueue.isEmpty():
        print('Queue Kosong')
    else:
        print('Queue tidak kosong. Isi: ', len(cobaQueue))
            
main()