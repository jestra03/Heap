# BST Tests [Data Structures]
# Joshua Estrada

import unittest
from binary_search_tree import *

class TestLab5(unittest.TestCase):

    def test_root(self):
        bst = BinarySearchTree()  # initialize BST
        self.assertTrue(bst.is_empty())  # BST is empty
        bst.insert(10, 'stuff')  # insert root
        self.assertTrue(bst.search(10))  # find node with key 10
        self.assertEqual(bst.find_min(), (10, 'stuff'))  # key 10 is min (only node)
        bst.insert(10, 'other')  # replace data in node with key 10
        self.assertEqual(bst.find_max(), (10, 'other'))  # key 10 is max (only node)

        # OTHER TESTS
        self.assertEqual(bst.preorder_list(), [10])  # PREORDER
        self.assertEqual(bst.inorder_list(), [10])  # INORDER
        self.assertEqual(bst.level_order_list(), [10])  # LEVEL ORDER
        self.assertEqual(bst.tree_height(), 0)  # HEIGHT

    def test_search_helper(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, "A")  # root is 10
        self.assertFalse(bst.is_empty())
        self.assertEqual(bst.find_min(), (10, "A"))
        bst.insert(5, "A")
        self.assertEqual(bst.find_min(), (5, "A"))
        self.assertEqual(bst.find_min(), (5, "A"))
        self.assertEqual(bst.find_max(), (10, "A"))
        bst.insert(15, "A")
        self.assertEqual(bst.find_max(), (15, "A"))
        bst.insert(25, "A")
        self.assertEqual(bst.find_max(), (25, "A"))
        bst.insert(0, "A")
        self.assertEqual(bst.find_min(), (0, "A"))

        bst.insert(10, "B")  # replace root
        self.assertEqual(bst.find_min(), (0, "A"))  # tree should be the same
        self.assertEqual(bst.find_max(), (25, "A"))

        bst.insert(0, "B")  # replace min data
        bst.insert(25, "B")  # replace max data
        self.assertEqual(bst.find_min(), (0, "B"))
        self.assertEqual(bst.find_max(), (25, "B"))

        bst.insert(5, "B")  # replace node at key 5
        bst.insert(10, "B")  # replace node at key 10

        self.assertTrue(bst.search(10))
        self.assertTrue(bst.search(5))
        self.assertTrue(bst.search(15))
        self.assertTrue(bst.search(0))
        self.assertTrue(bst.search(25))
        self.assertFalse(bst.search(30))

        # OTHER TESTS
        self.assertEqual(bst.preorder_list(), [10, 5, 0, 15, 25])  # PREORDER
        self.assertEqual(bst.inorder_list(), [0, 5, 10, 15, 25])  # INORDER
        self.assertEqual(bst.level_order_list(), [10, 5, 15, 0, 25])  # LEVEL ORDER
        self.assertEqual(bst.tree_height(), 2)  # HEIGHT

    def test_balanced_tree(self):
        bst = BinarySearchTree()
        bst.insert(25, "")
        bst.insert(20, "")
        bst.insert(15, "")
        bst.insert(23, "")
        bst.insert(30, "")
        bst.insert(27, "")
        bst.insert(35, "")
        # SEARCH TESTS
        self.assertTrue(bst.search(25))
        self.assertTrue(bst.search(20))
        self.assertTrue(bst.search(15))
        self.assertTrue(bst.search(23))
        self.assertTrue(bst.search(30))
        self.assertTrue(bst.search(27))
        self.assertTrue(bst.search(35))

        # OTHER TESTS
        self.assertEqual(bst.preorder_list(), [25, 20, 15, 23, 30, 27, 35])  # PREORDER
        self.assertEqual(bst.inorder_list(), [15, 20, 23, 25, 27, 30, 35])   # INORDER
        self.assertEqual(bst.level_order_list(), [25, 20, 30, 15, 23, 27, 35])  # LEVEL ORDER
        self.assertEqual(bst.tree_height(), 2)  # HEIGHT

        self.assertEqual(bst.find_min(), (15, ''))  # FIND MIN
        self.assertEqual(bst.find_max(), (35, ''))  # FIND MAX
        bst.insert(15, ":)")
        bst.insert(35, ":(")
        self.assertEqual(bst.find_min(), (15, ':)'))  # FIND MIN
        self.assertEqual(bst.find_max(), (35, ':('))  # FIND MAX

    def test_unbalanced_tree1(self):
        bst = BinarySearchTree()
        bst.insert(20, "A")
        bst.insert(15, "B")
        bst.insert(10, "D")
        bst.insert(5, "F")
        bst.insert(0, "G")
        bst.insert(16, "E")
        bst.insert(25, "C")

        # OTHER TESTS
        self.assertEqual(bst.preorder_list(), [20, 15, 10, 5, 0, 16, 25])  # PREORDER
        self.assertEqual(bst.inorder_list(), [0, 5, 10, 15, 16, 20, 25])  # INORDER
        self.assertEqual(bst.level_order_list(), [20, 15, 25, 10, 16, 5, 0])  # LEVEL ORDER
        self.assertEqual(bst.tree_height(), 4)  # HEIGHT

        self.assertEqual(bst.find_min(), (0, 'G'))  # FIND MIN
        self.assertEqual(bst.find_max(), (25, 'C'))  # FIND MAX
        bst.insert(0, ":)")
        bst.insert(25, ":(")
        self.assertEqual(bst.find_min(), (0, ':)'))  # FIND MIN
        self.assertEqual(bst.find_max(), (25, ':('))  # FIND MAX

    def test_unbalanced_tree2(self):
        bst = BinarySearchTree()
        bst.insert(0, "A")  # A
        bst.insert(6, "B")  # B
        bst.insert(1, "C")  # C
        bst.insert(5, "D")  # D
        bst.insert(2, "E")  # E
        bst.insert(4, "F")  # F
        bst.insert(3, "G")  # G
        self.assertEqual(bst.preorder_list(), [0, 6, 1, 5, 2, 4, 3])
        # PREORDER: A B C D E F G
        self.assertEqual(bst.inorder_list(), [0, 1, 2, 3, 4, 5, 6])
        # INORDER: A C E G F D B
        self.assertEqual(bst.level_order_list(), [0, 6, 1, 5, 2, 4, 3])  # LEVEL ORDER
        self.assertEqual(bst.tree_height(), 6)  # HEIGHT

        self.assertEqual(bst.find_min(), (0, 'A'))  # FIND MIN
        self.assertEqual(bst.find_max(), (6, 'B'))  # FIND MAX
        bst.insert(0, ":)")
        bst.insert(6, ":(")
        self.assertEqual(bst.find_min(), (0, ':)'))  # FIND MIN
        self.assertEqual(bst.find_max(), (6, ':('))  # FIND MAX

    def test_empty_tree(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())  # EMPTY
        self.assertEqual(bst.preorder_list(), [])  # PRE ORDER
        self.assertEqual(bst.inorder_list(), [])  # IN ORDER
        self.assertEqual(bst.level_order_list(), [])  # LEVEL ORDER
        self.assertFalse(bst.search(1))  # SEARCH
        self.assertEqual(bst.find_min(), None)  # FIND MIN
        self.assertEqual(bst.find_max(), None)  # FIND MAX
        self.assertEqual(bst.tree_height(), None)  # HEIGHT

    # 6 TESTS OF PREORDER, INORDER, LEVEL ORDER, HEIGHT


if __name__ == '__main__': 
    unittest.main()
