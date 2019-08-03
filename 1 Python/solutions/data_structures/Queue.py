# Queue.py
# Stack.py
'''
FIFO data structure (first in first out), like a queue in real life
'''

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        '''
        add item to the end of the queue
        '''
        self.queue.append(item)

    def dequeue(self):
        '''
        remove item from the front of the queue and return it
        '''
        return self.queue.pop(0)

    def isempty(self):
        '''
        returns if queue is empty
        '''
        return len(self.queue) == 0


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.queue) # [1, 2, 3]
    print(q.isempty()) # False
    print(q.dequeue()) # 1
    print(q.dequeue()) # 2
    print(q.dequeue()) # 3
    print(q.isempty()) # True