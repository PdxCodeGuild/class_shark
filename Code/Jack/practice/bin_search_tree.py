class Node():

    def __init__(self, value, parent=None, left=None, right=None):
        self.val = value
        self.l = left
        self.r = right
        self.parent = parent

class Tree():

    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root == None:
            self.root = Node(value)

    def _add(self, data, node):
        if data < node.v:
            if node.l is None:
                child = BST(data=data, parent=self)
                node.l = child
                return
            else:
                return node.l.add(data)
        else:
            if self.r is None:
                child = BST(data, self)
                node.r = child
                return
            else:
                return node.r.add(data)

    def search(self, data):
        if self.v is None:
            return f'Not Found'
        if self.v == data:
            return self
        if data < self.v:
            return self.l.search(data)
        else:
            return self.r.search(data)
