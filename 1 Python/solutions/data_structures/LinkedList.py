# LinkedList.py

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

    def __repr__(self):
        return f'Node({self.data})'


class LinkedList:
    def __init__(self):
        self.head = Node(None) # pointer to head of list
        self.tail = self.head  # pointer to tail of list
        self.size = 0

    def __repr__(self):
        ret = ''
        cur = self.head
        while cur.next:
            ret += str(cur.next) + '->' 
            cur = cur.next
        return ret + 'None'

    def add(self, data, index=None):
        """
        adds new node at index (default: adds at tail)
        """
        new_node = Node(data)
        if index is None or index == self.size - 1:
            self.tail.next = new_node  # add node to tail of list
            self.tail = self.tail.next # set pointer to new tail
        else:
            if index >= self.size:
                raise IndexError
            cur = self.head
            for i in range(index):
                cur = cur.next
            new_node.next = cur.next.next
        self.size += 1                 # increment size

    def find(self, data):
        """
        returns first node with matching data
        """
        cur = self.head
        count = 1
        while cur.next:
            if cur.data == data:
                # print(f'Found in {count} tries.')
                return cur
            cur = cur.next
            count += 1
        return f'No node matching query: {data}.'

    def remove(self, data):
        """
        removes node with data from list
        """
        cur = self.head
        while cur.next:
            if cur.next.data == data:
                temp = cur.next
                if temp == self.tail:    # if we are removing the tail
                    self.tail = cur      # reset tail pointer
                cur.next = cur.next.next # splice cur.next out of list
                self.size -= 1           # decrement size
                return f'Removed {temp}'
            cur = cur.next
        return f'No node matching query: {data}'


if __name__ == '__main__':
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    print(ll)
    print(ll.find(2))
    ll.remove(2)
    print(ll)
    print(ll.find(2))
    
