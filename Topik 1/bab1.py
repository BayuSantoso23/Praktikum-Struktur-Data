from bab1_bag import Bag

myBag = Bag()

myBag.add(19)
myBag.add(11)
myBag.add(12)
myBag.add(13)

print('Banyak data dalam bag: ')
print(len(myBag))

myBag.remove(19)
myBag.remove(11)

nilai = int(input("Tebak nilai yang disimpan dalam bag: "))

if nilai in myBag:
    print("Bag berisi nilai", nilai)
else:
    print("Bag tidak berisi nilai", nilai)
    
    for elm in myBag:
        print(elm)