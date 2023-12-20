from Node import Node


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __repr__(self):
        return f"Stack: {self.top}"

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.top = self.top.next
            self.size -= 1
            return data
        return None

    def peek(self):
        if self.top:
            return self.top.data
        return None

    def is_empty(self):
        return self.top is None

    def get_size(self):
        return self.size



