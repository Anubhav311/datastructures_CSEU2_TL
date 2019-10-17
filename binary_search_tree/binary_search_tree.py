import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        # set the value at the current node
        self.value = value
        # add ref to left child node
        self.left = None
        # add ref to right child node
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # LEFT CASE
        # check if the new node value is less than our current node's value
        if value < self.value:
            # if there is no left child
            if not self.left:
                # place the node here
                self.left = BinarySearchTree(value)
            # otherwise
            else:
                # repeat process for left
                self.left.insert(value)
        
        # RIGHT CASE
        # check if the new node's value is greater than or equal to the current node's value
        elif value >= self.value:
            # if there is no right child
            if not self.right:
                # place the node here
                BinarySearchTree(value)
            # otherwise
            else:
                # repeat process for right
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # BASE CASE

        # LEFT CASE

        # RIGHT CASE
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        # BASE CASE
        # if empty tree
            # return None

        # RECURSIVE APPROACH
        # if there is no right value
            # return the root value
        # return the get_max of the right node

        # ITERATIVE APPROACH
        # set a max value variable to keep track of max value
        # get a ref to current node
        # check if we are at a valid tree node
            # if our current value is greater than the max value
                # update the max value
            # move on to the next right node in the tree
            # setting the current node to the current nodes right
        # return our max value
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # base case

        # left case

        # right case
        pass

    # DAY 4 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
