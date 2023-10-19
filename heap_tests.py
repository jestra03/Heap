# Lab 7: Heap Tests
# Data Structures [CPE 202-03]
# Joshua Estrada

import unittest
from heap import *


class TestHeap(unittest.TestCase):
    def test_standard(self):
        test_heap = MaxHeap(50)


if __name__ == "__main__":
    unittest.main()
