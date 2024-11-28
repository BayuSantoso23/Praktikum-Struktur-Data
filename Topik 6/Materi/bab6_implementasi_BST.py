from bab6_class_BinTreeNode import inorderTrav
from bab6_class_binarysearchtree import BST

# Konstruksi binary search tree dari
# list [60, 12, 90, 4, 41, 71, 100, 1, 29, 84, 23, 37]
binSearchTree = BST()
data = [60, 12, 90, 4, 41, 71, 100, 1, 29, 84, 23, 37]

# Tambahkan elemen-elemen data ke binary search tree
for datum in data:
    binSearchTree.add(datum)

# Print node-node tree
print('BST pertama kali dibangun:')
inorderTrav(binSearchTree._root)
print()

# Tambahkan 30 ke tree
binSearchTree.add(30)

# Tampilkan ukuran tree
print('Ukuran tree =', len(binSearchTree))

# Cek apakah 32 ada di tree
print('32 ada di tree?')
if (32 in binSearchTree):
    print('32 ada di tree.')
else:
    print('32 tidak ada di tree.')

# Print node-node tree setelah penambahan
print('BST setelah penambahan nilai 30:')
inorderTrav(binSearchTree._root)
print()

# Tampilkan nilai minimum
print('Min =', binSearchTree.min())

# Remove 23 (node leaf)
binSearchTree.remove(23)

# Remove 71 (node dengan 1 child)
binSearchTree.remove(71)

# Remove 12 (node dengan 2 child)
binSearchTree.remove(12)

# Print tree terakhir
print('BST akhir:')
inorderTrav(binSearchTree._root)
print()

# Tampilkan ukuran tree akhir
print('Ukuran tree akhir =', len(binSearchTree))
