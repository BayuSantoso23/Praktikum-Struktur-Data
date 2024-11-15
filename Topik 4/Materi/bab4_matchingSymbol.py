from bab4_stackNode import Stack

def isMatched(expr):
    s = Stack()
    for char in expr:
        if char in '{[(':
            s.push(char)
        elif char in '}])':
            if s.isEmpty():
                return False
            else:
                left = s.pop()
                if (char == '}' and left != '{') or \
                    (char == ']' and left != '[') or \
                    (char == ')' and left != '('):
                    return False 
    return s.isEmpty()

def main():
    expr = input("Ketikkan sebuah ekspresi: ")
    if isMatched(expr) == True:
        print("Ekspresi yang Anda masukkan BENAR.")
    else:
        print("Ekspresi yang Anda masukkan SALAH.")
main()

                    