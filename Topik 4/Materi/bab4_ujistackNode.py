from bab4_stackNode import Stack

def main():
    PROMPT = 'Masukkan nilai integer (nilai negatif untuk mengakhiri): '
    
    myStack = Stack()
    
    if myStack.isEmpty:
        print('Stack kosong.')
    else:
        print('Stack tidak kosong.')
        
    nilai = int(input(PROMPT))
    while nilai >= 0:
        myStack.push(nilai)
        nilai = int(input(PROMPT))
    
    print('Panjang stack: ', end='')
    print(len(myStack))
    
    print('Top dari stack: ', end='')
    print(myStack.peek())
    
    print('Isi stack: ')
    while not myStack.isEmpty():
        nilai = myStack.pop()
        print(nilai)
        
main()