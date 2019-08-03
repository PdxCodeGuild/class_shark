# Stack.py
'''
LIFO data structure (last in first out)
'''

class Stack:
    def __init__(self):
        self.stack = []

    def __repr__(self):
        return str(self.stack)

    def __len__(self):
        return len(self.stack)

    def __bool__(self):
        return not self.isempty()

    def push(self, item):
        '''
        add item to the end of the stack
        '''
        self.stack.append(item)

    def pop(self):
        '''
        remove item from the end of the stack and return it
        '''
        return self.stack.pop()

    def peek(self):
        '''
        returns item at end of the stack
        '''
        return self.stack[-1]

    def isempty(self):
        '''
        returns if stack is empty
        '''
        return len(self.stack) == 0


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.stack)  # [1, 2, 3]
    print(s.isempty()) # False
    print(s.pop()) # 3
    print(s.pop()) # 2
    print(s.pop()) # 1
    print(s.isempty()) # True