class BST:
    def __init__(self):
        self._root = None
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def __contains__(self, nilaiDicari):
        return self._bstSearch(self._root, nilaiDicari) is not None
    
    def _bstSearch(self, subtree, target):
        if subtree is None:
            return None
        elif target < subtree.data:
            return self._bstSearch(subtree.left, target)
        elif target > subtree.data:
            return self._bstSearch(subtree.right, target)
        else:
            return subtree
        
    def min(self):
        nodeMinimum = self._bstMinimum(self._root)
        if nodeMinimum is None:
            return 0
        return nodeMinimum.data
    
    def _bstMinimum(self, subtree):
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self._bstMinimum(subtree.left)
        
    def add(self, data):
        node = self._bstSearch(self._root, data)
        
        if node is not None:
            return False
        else:
            self._root = self._bstInsert(self._root, data)
            self._size += 1
            return True
        
    def _bstInsert(self, subtree, data):
        if subtree is None:
            subtree = _BSTNode(data)
        elif (data < subtree.data):
            subtree.left = self._bstInsert(subtree.left, data)
        elif (data > subtree.data):
            subtree.right = self._bstInsert(subtree.right, data)
        return subtree
    
    def remove(self, dataDihapus):
        if dataDihapus not in self:
            raise ValueError("Data tidak ditemukan")
        else:
            self._root = self._bstRemove(self._root, dataDihapus)
            self._size -= 1
            
    def _bstRemove(self, subtree, target):
        if subtree is None:
            return subtree
        elif target < subtree.data:
            subtree.left = self._bstRemove(subtree.left, target)
            return subtree
        elif target > subtree.data:
            subtree.right = self._bstRemove(subtree.right, target)
            return subtree
        else:
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is None or subtree.right is None:
                if subtree.left is None: 
                    return subtree.left
                else:
                    return subtree.right
            else:
                successor = self._bstMinimum(subtree.right)
                subtree.data = successor.data
                subtree.right = self._bstRemove(subtree.right, successor.data)
                return subtree

class _BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None