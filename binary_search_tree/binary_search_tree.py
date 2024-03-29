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
        # if value of the current node matches the target, we have found a match
        if self.value == target:
            return True

        # LEFT CASE
        # if there is a left child, do a recursive call to contains on left
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)

        # RIGHT CASE
        # if there is a right child, do a recursive call to contains on right
        if target >= self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # BASE CASE
        # if empty tree
        if not self:
            # return None
            return None

        # # RECURSIVE APPROACH
        # # if there is no right value
        # if not self.right:
        #     # return the root value
        #     return self.value
        # # return the get_max of the right node
        # return self.right.get_max()

        # ITERATIVE APPROACH
        # set a max value variable to keep track of max value
        max_value = self.value
        # get a ref to current node
        current_node = self
        # check if we are at a valid tree node
        while current_node:
            # if our current value is greater than the max value
            if current_node.value > max_value:
                # update the max value
                max_value = current_node.value
            # move on to the next right node in the tree
            # setting the current node to the current nodes right
            current_node = current_node.right
        # return our max value
        return max_value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # base case
        cb(self.value)

        # left case
        if self.left:
            self.left.for_each(cb)
        # right case
        if self.right:
            self.right.for_each(cb)

    def itter_def_for_each(self, cb):
        # create a new stack to hold our traversal data
        stack = []
        # pushing the root node onto the stack
        stack.append(self)
        # while there are still nodes on the stack
        while len(stack):
            # pop the current node off the stack
            current_node = stack.pop()
            # if current node has a child
            if current_node.right:
                # push the current nodes right node onto the stack
                stack.append(current_node.right)
            # if the current node has a left child
            if current_node.left:
                # push the current nodes left node onto the stack
                stack.append(current_node.left)
            # call the call back on the current nodes value
            cb(current_node.value)

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
