# from dll_stack import Stack
# from dll_queue import Queue
import sys
# sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Which direction to go?
        if value < self.value:
            # Traverse left
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            # Traverse right
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
            

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        else:
            if self.left:
                return self.left.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        self.value = cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.left.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.right.in_order_print(node.right)

    # # Print the value of every node, starting with the given node,
    # # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     # Create queue
    #     queue = Queue()
    #     # Add node to queue
    #     queue.enqueue(node)

    #     while queue.len() > 0:
    #         target = queue.dequeue()
    #         print(target.value)
    #         if target.right:
    #             queue.enqueue(target.right)
    #         if target.left:
    #             queue.enqueue(target.left)

    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # def dft_print(self, node):
    #     # Create stack
    #     stack = Stack()
    #     # Add node to stack
    #     stack.push(node)

    #     while stack.len() > 0:
    #         target = stack.pop()
    #         print(target.value)
    #         if target.right:
    #             stack.push(target.right)
    #         if target.left:
    #             stack.push(target.left)

    # # STRETCH Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT

    # def pre_order_dft(self, node):
    #     # Create stack
    #     stack = Stack()
    #     # Add node to stack
    #     stack.push(node)

    #     while stack.len() > 0:
    #         target = stack.pop()
    #         print(target.value)
    #         if target.right:
    #             stack.push(target.right)
    #         if target.left:
    #             stack.push(target.left)

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     if node.left:
    #         self.post_order_dft(node.left)
    #     if node.right:
    #         self.post_order_dft(node.right)
    #     print(node.value)
