import bab6_class_BinTreeNode as btree

# Membuat binary tree
root = btree._BinTreeNode('A')

root.left = btree._BinTreeNode('B')
root.left.left = btree._BinTreeNode('D')
root.left.right = btree._BinTreeNode('E')
root.left.right.left = btree._BinTreeNode('H')
root.right = btree._BinTreeNode('C')
root.right.left = btree._BinTreeNode('F')
root.right.right = btree._BinTreeNode('G')
root.right.right.left = btree._BinTreeNode('I')
root.right.right.right = btree._BinTreeNode('J')

# Preorder traversal
print('Preorder traversal:')
btree.preorderTrav(root)
print()

# Inorder traversal
print('Inorder traversal:')
btree.inorderTrav(root)
print()

# Postorder traversal
print('Postorder traversal:')
btree.postorderTrav(root)
print()

# Breadth-First traversal
print('Breadth-First traversal:')
btree.breadthfirstNav(root)
print()
