from bab2_array2d import Array2D

import random

daftarNilai = Array2D(5,5)

for i in range(daftarNilai.bykBaris()):
    for j in range(daftarNilai.bykKolom()):
        daftarNilai[i, j] = random.randint(0, 100)
        
for i in range(daftarNilai.bykBaris()):
    for j in range(daftarNilai.bykKolom()):
        print(f'{daftarNilai[i,j]:3d}', end = ' ')
    print('\n')
    
print('Banyak baris: ', end=' ')
print(daftarNilai.bykBaris())

print('Banyak kolom: ', end=' ')
print(daftarNilai.bykKolom())

daftarNilai.clear(10)

print()
print('Isi array setelah clear dengan 10: ')
for i in range(daftarNilai.bykBaris()):
    for j in range(daftarNilai.bykKolom()):
        print(f'{daftarNilai[i, j]:3d}', end=' ')
    print('\n')
    
try:
    print(daftarNilai[4, 7])
except IndexError:
    print('Indeks tidak valid.')
    
try:
    print(daftarNilai[4, 3, 4])
except IndexError:
    print('Banyak indeks tidak valid.')