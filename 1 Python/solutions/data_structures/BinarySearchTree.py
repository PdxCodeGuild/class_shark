class BST:
    def __init__(self, data=None, parent=None, left_child=None, right_child=None):
        self.data = data
        self.parent = parent
        self.left = left_child
        self.right = right_child

    def __repr__(self):
        return str(self.data)

    def tree_dict(self):
        '''
        recursively represent tree as dictionary
        '''
        if self.left:
            left = self.left.tree_dict()
        else:
            left = None
        if self.right:
            right = self.right.tree_dict()
        else:
            right = None
        return {self.data: [left, right]}

    def add(self, data):
        '''
        recursively add node to BST by following this simple rule
        '''
        if data < self.data:
            if self.left is None:
                child = BST(data=data, parent=self)
                self.left = child
                return
            else:
                # recursively find next available node on left side of tree
                return self.left.add(data)
        else:
            if self.right is None:
                child = BST(data, self)
                self.right = child
                return
            else:
                # recursively find next available node on right side of tree
                return self.right.add(data)

    def search(self, data):
        '''
        recursively traverse BST in search of target data
        '''
        print('Node:', self.data, 'Target:', data)
        if self.data == data:
            return self
        if data < self.data and self.left:
            print('Searching left...')
            return self.left.search(data)
        elif self.right:
            print('Searching right...')
            return self.right.search(data)
        else:
            return 'Not Found'


if __name__ == '__main__':
    bst = BST(5)
    bst.add(6)
    bst.add(7)
    bst.add(8)
    bst.add(3)
    bst.add(4)
    bst.add(1)
    bst.add(2)
    bst.add(9)
    print(bst.tree_dict())
    print(bst.search(13))
    print(bst.search(4))
    print(bst.search(8))







