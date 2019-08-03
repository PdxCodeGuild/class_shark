class Node(object):
    """docstring for Node."""


    def __init__(self, value):
        self.right_node = None
        self.left_node = None
        self.value = value


class Tree(object):
    """docstring for Tree."""

    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.value:
            if node.left_node is not None:
                self._add(val, node.left_node)
            else:
                node.left_node = Node(val)
        else:
            if node.right_node is not None:
                self._add(val, node.right_node)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.value:
            return node
        elif val < node.value and node.left_node is not None:
            self._find(val, node.left_node)
        elif val > node.value and node.right_node is not None:
            self._find(val, node.right_node)

    def delete_tree(self):
        self.root = None

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left_node)
            print(f'{node.value} ')
            self._print_tree(node.right_node)


tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.print_tree()
print(tree.find(3))
print(tree.find(10))
tree.delete_tree()
tree.print_tree()
