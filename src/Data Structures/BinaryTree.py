from Queue import Queue


class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

    def __repr__(self):
        return f"BinaryTree: {self.root}"

    def insert_left(self, data):
        if self.left is None:
            self.left = BinaryTree(data)
        else:
            tree = BinaryTree(data)
            tree.left = self.left
            self.left = tree

    def insert_right(self, data):
        if self.right is None:
            self.right = BinaryTree(data)
        else:
            tree = BinaryTree(data)
            tree.right = self.right
            self.right = tree

    def DFS(self):
        print(self.root)
        if self.left:
            self.left.DFS()
        if self.right:
            self.right.DFS()

    def BFS(self):
        queue = Queue()
        queue.enqueue(self)
        while not queue.is_empty():
            current = queue.dequeue()
            print(current.root)
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)



