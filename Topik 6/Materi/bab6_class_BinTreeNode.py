from bab6_class_linkedListQueue import Queue


class _BinTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorderTrav(subtree):
    if subtree is not None:
        print(subtree.data, end=" ")
        preorderTrav(subtree.left)
        preorderTrav(subtree.right)


def inorderTrav(subtree):
    if subtree is not None:
        inorderTrav(subtree.left)
        print(subtree.data, end=" ")
        inorderTrav(subtree.right)


def postorderTrav(subtree):
    if subtree is not None:
        postorderTrav(subtree.left)
        postorderTrav(subtree.right)
        print(subtree.data, end=" ")


def breadthfirstNav(root):
    q = Queue()
    q.enqueue(root)

    while not q.isEmpty():
        node = q.dequeue()

        print(node.data, end=" ")

        if node.left is not None:
            q.enqueue(node.left)
        if node.right is not None:
            q.enqueue(node.right)
