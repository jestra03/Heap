# Heap [Data Structures]
# Joshua Estrada


import unittest
from heap import *


class TestHeap(unittest.TestCase):
    def test_standard(self):
        heap = MaxHeap(50)
        heap.enqueue(1)
        heap.enqueue(20)
        heap.enqueue(9)
        heap.enqueue(81)
        heap.enqueue(2)
        heap.enqueue(27)
        heap.enqueue(15)
        heap.enqueue(3)
        self.assertEqual(heap.contents(), [81, 20, 27, 3, 2, 9, 15, 1])
        heap.dequeue()
        self.assertEqual(heap.contents(), [27, 20, 15, 3, 2, 9, 1])

    def test_build_heap(self):
        heap = MaxHeap()
        heap.build_heap([1, 20, 9, 81, 2, 27, 15, 3])
        exp = [81, 20, 27, 3, 2, 9, 15, 1]  # done by hand (white-boarding)
        self.assertEqual(heap.contents(), exp)

        heap.build_heap_alternative([1, 20, 9, 81, 2, 27, 15, 3])
        exp = [81, 20, 27, 3, 2, 9, 15, 1]  # done by hand (white-boarding)
        self.assertEqual(heap.contents(), exp)


if __name__ == "__main__":
    unittest.main()
