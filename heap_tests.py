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
        self.assertTrue(heap.enqueue(3))
        self.assertEqual(heap.contents(), [81, 20, 27, 3, 2, 9, 15, 1])
        self.assertEqual(heap.dequeue(), 81)
        self.assertEqual(heap.contents(), [27, 20, 15, 3, 2, 9, 1])

    def test_build_heap(self):
        heap = MaxHeap()
        heap.build_heap([1, 20, 9, 81, 2, 27, 15, 3])
        exp = [81, 20, 27, 3, 2, 9, 15, 1]  # done by hand (white-boarding)
        self.assertEqual(heap.contents(), exp)

        heap.build_heap_alternative([1, 20, 9, 81, 2, 27, 15, 3])
        exp = [81, 20, 27, 3, 2, 9, 15, 1]  # done by hand (white-boarding)
        self.assertEqual(heap.contents(), exp)

    def test_heapsort(self):
        heap = MaxHeap()
        arr = [1, 20, 9, 81, 2, 27, 15, 3]
        arr = heap.heapsort(arr)
        self.assertEqual(arr, [1, 2, 3, 9, 15, 20, 27, 81])

        arr = heap.heapsort_decending([1, 20, 9, 81, 2, 27, 15, 3])
        self.assertEqual(arr, [81, 27, 20, 15, 9, 3, 2, 1])

if __name__ == "__main__":
    unittest.main()
