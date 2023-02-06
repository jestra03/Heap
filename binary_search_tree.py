# BST [Data Structures]
# Joshua Estrada

from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None
        # initializes empty BST

    def is_empty(self): 
        return self.root is None
        # returns True if tree is empty, else False

    def search(self, key):
        if self.is_empty():
            return False
        return self.search_helper(self.root, key)
        # returns True if key is in a node of the tree, else False
        # calls recursive helper method

    def search_helper(self, node, key):
        if node == None:
            return False
        if key == node.key:  # base case [is found]
            return True
        if key < node.key:
            return self.search_helper(node.left, key)
        return self.search_helper(node.right, key)
        # returns True if key is found in BST
        # returns False if key not found in BST

    def insert(self, key, data=None):
        if self.is_empty():  # insert root
            self.root = TreeNode(key, data)
        elif self.root.key == key:  # replace root node if key is the same
            left = self.root.left
            right = self.root.right
            self.root = TreeNode(key, data, left, right)
        self.insert_helper(self.root, key, data)
        # calls recursive method

    def insert_helper(self, node, key, data):
        if key < node.key:
            if node.left == None:  # add new left
                node.left = TreeNode(key, data)
                return True
            elif node.left.key == key:  # replace
                left = node.left.left
                right = node.left.right
                node.left = TreeNode(key, data, left, right)
            return self.insert_helper(node.left, key, data)  # go left
        if key > node.key:
            if node.right == None:  # add new right
                node.right = TreeNode(key, data)
                return True
            elif node.right.key == key:
                left = node.right.left
                right = node.right.right
                node.right = TreeNode(key, data, left, right)
            return self.insert_helper(node.right, key, data)
        # inserts new node [with key and data]
        # if there is a node with same key, its data will be replaced by new data

    def find_min(self):
        if self.is_empty():
            return None
        return self.find_min_helper(self.root)
        # returns None if the tree is empty
        # calls recursive helper method

    def find_min_helper(self, node):
        if node.left == None:  # outermost left node reached
            return node.key, node.data  # return min node
        return self.find_min_helper(node.left)  # call next left node
        # returns a tuple with min key and data in the BST

    def find_max(self):
        if self.is_empty():
            return None
        return self.find_max_helper(self.root)
        # returns None if the tree is empty
        # calls recursive helper method

    def find_max_helper(self, node):
        if node.right == None:  # outermost right node reached
            return node.key, node.data  # return max node
        return self.find_max_helper(node.right)  # call next right node
        # returns a tuple with max key and data in the BST

    def tree_height(self):
        if self.is_empty():
            return None
        return self.tree_height_helper(self.root) - 1
        # return the height of the tree
        # returns None if tree is empty
        # calls recursive helper method

    def tree_height_helper(self, node):
        if node == None:  # end of tree
            return 0
        return 1 + max(self.tree_height_helper(node.left), self.tree_height_helper(node.right))
        # helper method which counts tree depth on particular subtree recursively

    def inorder_list(self):
        if self.is_empty(): return []  # return empty list if empty
        in_lst = []
        in_lst += self.in_helper(self.root.left)
        in_lst.append(self.root.key)
        in_lst += self.in_helper(self.root.right)
        return in_lst
        # return Python list of BST keys representing in-order traversal of BST
        # calls recursive helper method

    def in_helper(self, node):
        if node == None:
            return []
        return self.in_helper(node.left) + [node.key] + self.in_helper(node.right)  # traverse by in_order
        # helper method which returns in_order list of BST using recursion

    def preorder_list(self):
        if self.is_empty(): return []  # return empty list if empty
        in_lst = []
        in_lst.append(self.root.key)
        in_lst += self.pre_helper(self.root.left)
        in_lst += self.pre_helper(self.root.right)
        return in_lst
        # return Python list of BST keys representing pre-order traversal of BST
        # calls recursive helper method

    def pre_helper(self, node):
        if node == None:
            return []
        return [node.key] + self.pre_helper(node.left) + self.pre_helper(node.right)  # traverse by pre_order
        # helper method which returns pre_order list of BST using recursion

    def level_order_list(self):
        q = Queue(25000)  # Don't change this! ok
        if self.is_empty():  # return empty list if empty
            return []
        q.enqueue(self.root)
        lvl_order_lst = []
        while True:
            node = q.items[q.front]
            if node.left != None:  # enqueue its child nodes
                q.enqueue(node.left)
            if node.right != None:
                q.enqueue(node.right)
            lvl_order_lst.append(q.dequeue().key)  # dequeue front append accordingly
            if q.is_empty():
                return lvl_order_lst
        # return Python list of BST keys representing level-order traversal of BST
