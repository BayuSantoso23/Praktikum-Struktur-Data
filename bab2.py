from bab2_array1d import Array

daftarNilai = Array(5)

daftarNilai[0] = 90
daftarNilai[1] = 78
daftarNilai[2] = 89
daftarNilai[3] = 67
daftarNilai[4] = 73

print ('Panjang array: ', end='')
print(len(daftarNilai))

print(daftarNilai[1])

print('Nilai array: ')
for nilai in daftarNilai:
    print(nilai, end=' ')
print()
    
daftarNilai.clear(10)

print('Nilai array setelah clear dengan nilai 10: ')
for nilai in daftarNilai:
    print(nilai, end=' ')
print()

try:
    print(daftarNilai[-1])
except IndexError:
    print('Indeks -1 bulan indeks yang valid.')
    
try:
    daftarNilai[5]
except IndexError:
    print('Array tidak mempunyai indeks 5.')
    



