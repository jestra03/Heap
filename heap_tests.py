# Lab 7: Heap Tests
# Data Structures [CPE 202-03]
# Joshua Estrada

import unittest
from heap import *


class TestHeap(unittest.TestCase):
    def test_01_enqueue(self):
        test_heap = MaxHeap(7)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])

    def test_02_dequeue(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])



if __name__ == "__main__":
    unittest.main()
