class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_value):
        self.insert_helper(self.root, new_value)

    def insert_helper(self, current, new_value):
        if current.value < new_value:
            if current.right:
                self.insert_helper(current.right, new_value)
            else:
                current.right = Node(new_value)
        else:
            if current.left:
                self.insert_helper(current.left, new_value)
            else:
                current.left = Node(new_value)

    def search(self, value):
        return self.search_helper(self.root, value)

    def search_helper(self, current, value):
        if current:
            if current.value == value:
                return True
            elif current.value < value:
                return self.search_helper(current.right, value)
            else:
                return self.search_helper(current.left, value)

    def is_bst_satisfied(self):
        def helper(current, lower=float('-inf'), upper=float('inf')):
            if not current:
                return True

            val = current.value

            if val <= lower or val >= upper:
                return False
            
            if not helper(current.right, val, upper):
                return False
            if not helper(current.left, lower, val):
                return False
            return True

        return helper(self.root)

