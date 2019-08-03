class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node: {self.data}, next = {self.next}'


class LinkedList():
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        new_node = Node(data)
        current_node.next = new_node

    def find(self, data):
        current_node = self.head
        while current_node.next:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return f'Not Found'

    def delete(self, data):
        prev_node = self.head
        current_node = self.head.next
        while current_node.next:
            if current_node.data == data:
                prev_node.next = current_node.next
                current_node.next = None
            else:
                prev_node = current_node
                current_node = current_node.next

    def __repr__(self):
        ret = ''
        current_node = self.head
        while current_node:
            ret += f'{current_node.data} ->'
            current_node = current_node.next
        return ret + ' null'


if __name__ == '__main__':
    ll = LinkedList(1)
    ll.add(2)
    ll.add(22)
    ll.add(3)
    print(ll)
    ll.delete(22)
    print(ll)
