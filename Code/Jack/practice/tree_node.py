'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Variations of the Tree data structure include Binary Search Trees (left-right
sorted trees with at most two children, excellent for searching), heaps
(top-down sorted trees, good for min, max), and Red-Black Trees
(self-balancing BST). We won't delve much on those here, but it's well worth a
read!
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


class Tree():
    """docstring for Tree."""

    def __init__(self, data, children=None, parent=None):
        self.data = data
        self.children = children
        self.parent = parent

    def add_child(self, data):
        child = Tree(data, parent=self)
        self.children.append(child)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''   OR   '''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


from collections import defaultdict
def Tree():
    return defaultdict(Tree)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''   send to json   ''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import json
print(json.dumps(tree)) # {"1": {"2": {"5":6}, "3": 7, "4": {"8":{}, "9": {}}}}
