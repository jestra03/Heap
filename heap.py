# Heap [Data Structures]
# Joshua Estrada


class MaxHeap:
    def __init__(self, capacity=50):
        self.capacity = capacity
        self.heap = [None] + [None] * capacity  # allocate new arr for heap (0 index not included)
        self.size = 0

    def enqueue(self, item):
        if self.is_full():
            return False
        self.size += 1
        self.heap[self.size] = item  # add node to end
        self.perc_up(self.size)  # insert (perc_up, upwards)
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        val = self.heap[1]  # save max
        self.heap[1] = self.heap[self.size]  # set root node to end node
        self.size -= 1  # end node is in "garbage collector"
        self.perc_down(1)  # insert (perc_down, downwards)
        return val

    def build_heap(self, arr: list):
        self.heap = [None] + arr
        self.size = self.capacity = len(arr)
        for i in range(len(arr), 0, -1):
            self.perc_down(i)
        return True
    # bottom-up construction || O(nlogn)
    # replaces initialized capacity with length of new list

    def perc_up(self, i):
        while i // 2 != 0 and self.heap[i // 2] < self.heap[i]:
            self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]  # swap
            i = i // 2  # follow node
        return True
    # will continue percolating until it has reached root (index 1) or the parent is greater than child node (inserted)
    # index of node is tracked as parent and child are swapped

    def perc_down(self, i):
        while i * 2 < self.size + 1:  # while left child
            if i * 2 + 1 < self.size + 1:  # if right child also
                if self.heap[i] < self.heap[i * 2] and self.heap[i * 2] >= self.heap[i * 2 + 1]:
                    self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                    i = i * 2
                elif self.heap[i] < self.heap[i * 2 + 1] and self.heap[i * 2] < self.heap[i * 2 + 1]:
                    self.heap[i], self.heap[i * 2 + 1] = self.heap[i * 2 + 1], self.heap[i]
                    i = i * 2 + 1
                else:  # both children are smaller, parent is max
                    break
            elif self.heap[i] < self.heap[i * 2]:
                self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                i = i * 2
            else:
                break
        return True

    def build_heap_alternative(self, arr: list):
        self.heap = [None] + [None]*len(arr)  # clear previous heap (will replace with new heap)
        self.size = 0
        self.capacity = len(arr)  # new capacity
        for i in range(len(arr)):
            self.heap[i + 1] = arr[i]
            self.perc_up(i + 1)  # insert element
            self.size += 1
        return True
    # top-down construction || O(n)
    # replaces initialized capacity with length of new list

    def contents(self):
        return self.heap[1:self.size + 1]

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity
