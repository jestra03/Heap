# Queue Array

class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = self.back = self.num_items = 0

    def is_empty(self):
        return self.num_items == 0

    def is_full(self):
        return self.num_items == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise IndexError
        self.items[self.back] = item
        if self.back == self.capacity - 1:
            self.back = 0
        else:
            self.back += 1
        self.num_items += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError
        removed = self.items[self.front]
        if self.front == self.capacity - 1:
            self.front = 0
        else:
            self.front += 1
        self.num_items -= 1
        return removed

    def size(self):
        return self.num_items
