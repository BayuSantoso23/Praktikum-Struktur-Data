from bab5_class_Queue import Queue

def main():
    cobaQueue = Queue()
    
    if cobaQueue.isEmpty():
        print("Queue Kosong")
    else:
        print("Queue tidak kosong")
        
    input_data = 'Masukkan nilai integer (nilai negatif untuk mengakhiri): '
    
    nilai = int(input(input_data))
    
    while nilai > 0:
        cobaQueue.enqueue(nilai)
        nilai = int(input(input_data))
            
    print('Panjang queue: ', end='')
    print(len(cobaQueue))
    
    print('Isi Queue')
    while not cobaQueue.isEmpty():
        nilai = cobaQueue.dequeue()
        if not cobaQueue.isEmpty():
            print(nilai, end=' ')
        else:
            print(nilai)
            
main()