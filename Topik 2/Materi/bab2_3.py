from bab2_matriks import Matriks
from random import randint

def cetakMatriks(matriks):
    for brs in range(matriks.bykBaris()):
        for klm in range(matriks.bykKolom()):
            print(f'{matriks[brs, klm]: 4d}', end=' ')
        print()
        
def main():
    matrix1 = Matriks(3, 4)
    
    for i in range(matrix1.bykBaris()):
        for j in range(matrix1.bykKolom()):
            matrix1[i, j] = randint(0, 100)
            
    print('Matrix 1:')
    cetakMatriks(matrix1)
    print()
    
    matrixTranspose = matrix1.transpos()
    print('Transpose matrix 1:')
    cetakMatriks(matrixTranspose)
    print()
    
    matrix2 = Matriks(3, 4)
    
    for i in range(matrix2.bykBaris()):
        for j in range(matrix2.bykKolom()):
            matrix2[i, j] =  randint(0, 100)
        
    print('Matrix 2:')
    cetakMatriks(matrix2)
    print()
    
    jumlahMatrix = matrix2 + matrix1
    
    print('Matrix1 + Matrix2:')
    cetakMatriks(jumlahMatrix)
    print()
    
    selisihMatrix = matrix1 - matrix2
    
    print('Matrix1 - Matrix2:')
    cetakMatriks(selisihMatrix)
    print()
    
    MatrixA = Matriks(2, 3)
    MatrixA[0, 0] = 1
    MatrixA[0, 1] = 2
    MatrixA[0, 2] = 3
    MatrixA[1, 0] = 4
    MatrixA[1, 1] = 5
    MatrixA[1, 2] = 6
    
    print('Matrix A:')
    cetakMatriks(MatrixA)
    print()

    MatrixB = Matriks(2, 3)
    MatrixB[0, 0] = 7
    MatrixB[0, 1] = 8
    MatrixB[0, 2] = 9
    MatrixB[1, 0] = 10
    MatrixB[1, 1] = 11
    MatrixB[1, 2] = 12
    
    print('Matrix B:')
    cetakMatriks(MatrixB)
    print()
    
    print('Hasil kali matrix A dan matrix B: ')
    cetakMatriks(MatrixA * MatrixB)
    print()
    
main()