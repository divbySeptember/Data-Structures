"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    """
    Display the whole tree. Uses recursive def.
    """
    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None: 
            print ('-' * level * 2, pref, self.node.key,
                   f'[{self.height}:{self.balance}]',
                   'L' if self.height == 0 else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

    """
    Computes the maximum number of levels there are
    in the tree
    """
    def update_height(self):
        left = self.node.left
        right = self.node.right
        left_height = 0
        right_height = 0

        if left:
            left.update_height()
            left_height = left.height
        if right:
            right.update_height()
            right_height = right.height
        if left_height > right_height:
            self.height = left_height + 1
        else:
            self.height = right_height + 1
        return self.height

    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        if self.node is not None:
            left = self.node.left
            right = self.node.right
            left_height = 0
            right_height = 0

            if left:
                left.update_balance()
                left_height = left.height
            if right:
                right.update_balance()
                right_height = right.height
            
            self.balance = left_height - right_height
            return self.balance

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """
    def left_rotate(self):
        if self.node.right:
            child = self.node.right
            self.node.right = None
            child.node.left = self

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self):
        if self.node.left:
            child = self.node.left
            self.node.left = None
            child.node.right = self

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    def rebalance(self):
        if self.balance > 1:
            if self.node.right.balance > 0:
                self.left_rotate()
            else:
                self.node.right.right_rotate()
                self.rebalance()
        elif self.balance < -1:
            if self.node.left.balance > 0:
                self.right_rotate()
            else:
                self.node.left.left_rotate()
                self.rebalance()

        
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def insert(self, key):
        if self.node is not None:
            if key < self.node.key:
                if self.node.left:
                    self.node.left.insert(key)
                else:
                    self.node.left = AVLTree(Node(key))
            else:
                if self.node.right:
                    self.node.right.insert(key)
                else:
                    self.node.right = AVLTree(Node(key))
        else:
            self.node = Node(key)
        self.update_balance()
        if abs(self.balance) > 1:
            self.rebalance()
