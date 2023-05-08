from queue import Queue
from stack import Stack

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    # depth-first search in binary tree:
    # pre-order
    # in-order
    # post-order

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(self.root)
        elif traversal_type == "reverse_levelorder":
            return self.reverse_levelorder_print(self.root)

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal    

    def levelorder_print(self, start):
        """Level order binary tree traversal. BFS"""
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)
        traversal = ""

        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

    def reverse_levelorder_print(self, start):
        """Reverse level order binary tree traversal"""
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)
        traversal = ""

        stack = Stack()

        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"

        return traversal

    def height(self, start):
        """Returns the height of binary tree"""
        if node is None:
            return -1

        left_height = height(node.left)
        right_height = height(node.right)

        return 1 + max(left_height, right_height)

    def size(self, node):
        """Return total number of nodes in binary tree"""
        if node is None:
            return int(0)

        # will use level order traversal to count all elements
        queue = Queue()
        queue.enqueue(node)
        count = 0

        while len(queue) > 0:
            count += 1
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return count
        
        #iterative approach

    def size_iterative(self, node):
        """Same as size() but using iterative approach"""
        if node is None:
            return 0
        stack = Stack()
        stack.push(node)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)
        return size

    def size_recursive(self, node):
        """Recursive counting of total number of nodes in binary tree"""
        is node is None:
            return 0
        return 1 + self.size_recursive(node.left) + self.size_recursive(node.right)
