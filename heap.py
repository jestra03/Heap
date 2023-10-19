# Heap [Data Structures]
# Joshua Estrada


class MaxHeap:
    def __init__(self, capacity=50):
        self.capacity = capacity
        self.heap = [None] + [None]*capacity  # allocate new arr for heap (0 index not included)
        self.size = 0

    def build_heap(self, arr: list):
        self.heap = [None] + [None]*len(arr)  # clear previous heap (will replace with new heap)
        self.size = 0
        for i in range(len(arr)):
            self.heap[i + 1] = arr[i]
            self.perc_up(i + 1)  # insert element
            self.size += 1
        return True
    # bottom up construction

    def perc_up(self, i):
        while i // 2 != 0 and self.heap[i // 2] < self.heap[i]:
            self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]  # swap
            i = i // 2  # follow node
        return True
    # will continue percolating until it has reached root (index 1) or the parent is greater than child node (inserted)
    # index of node is tracked as parent and child are swapped

    def contents(self):
        return self.heap[1:]
