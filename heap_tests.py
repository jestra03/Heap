# Lab 7: Heap Tests
# Data Structures [CPE 202-03]
# Joshua Estrada

import unittest
from heap import *


class TestHeap(unittest.TestCase):
    def test_standard(self):
        heap = MaxHeap(50)
        heap.build_heap([1, 20, 9, 81, 2, 27, 15, 3])
        exp = [81, 20, 27, 3, 2, 9, 15, 1]  # done by hand (white-boarding)
        self.assertEqual(heap.contents(), exp)


if __name__ == "__main__":
    unittest.main()
