input_data = 'Masukkan nilai integer (nilai negatif untuk mengakhiri): '
    
    nilai = int(input(input_data))
    
    while nilai > 0:
        cobaQueue.enqueue(nilai)
        nilai = int(input(input_data))