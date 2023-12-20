from Node import *


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.prev = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node
        self.size += 1

    def insert(self, data, index):
        if index < 0 or index > self.size:
            raise Exception("Index out of bounds")
        node = Node(data)
        if index == 0:
            node.next = self.head
            self.head = node
            self.size += 1
            return
        current = self.head
        i = 0
        while current:
            if i == index - 1:
                node.next = current.next
                current.next = node
                if node.next is None:
                    self.tail = node
                self.size += 1
                return
            current = current.next
            i += 1

    def remove(self, data):
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                self.size -= 1
                return True
            previous = current
            current = current.next
        return False

    def remove_by_index(self, index):
        if index < 0 or index >= self.size:
            raise Exception("Index out of bounds")
        current = self.head
        previous = None
        i = 0
        while current:
            if i == index:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                self.size -= 1
                return True
            previous = current
            current = current.next
            i += 1
        return False

    def get_size(self):
        return self.size

    def __repr__(self):
        current = self.head
        nodes = []
        while current:
            nodes.append(repr(current))
            current = current.next
        return ",".join(nodes)

    def search_by_data(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def search_by_node(self, node):
        current = self.head
        while current:
            if current == node:
                return current
            current = current.next
        return None

