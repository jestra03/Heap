# Heap [Data Structures]
# Joshua Estrada


class MaxHeap:
    def __init__(self, capacity=50):
        self.capacity = capacity
        self.heap = [None] + [None]*capacity  # allocate new arr for heap (0 index not included)
        self.size = 0

