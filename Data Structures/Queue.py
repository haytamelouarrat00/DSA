from Node import Node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        return f"Queue: {self.head}"

    def enqueue(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node
        self.size += 1

    def dequeue(self):
        if self.head:
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return data
        return None

    def peek(self):
        if self.head:
            return self.head.data
        return None

    def is_empty(self):
        return self.head is None

    def get_size(self):
        return self.size


