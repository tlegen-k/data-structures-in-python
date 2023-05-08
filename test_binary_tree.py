from binary_tree import Node, BinaryTree
# 1-2-4-5-3-6-7-
# 4-2-5-1-6-3-7
# 4-5-2-6-7-3-1
#               1
#           /       \  
#          2          3  
#         /  \      /   \
#        4    5     6   7 

# Set up tree:
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
#tree.root.right.left = Node(6)
#tree.root.right.right = Node(7)

#print(tree.print_tree("preorder"))
#print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
print(tree.print_tree("levelorder"))
print(tree.print_tree("reverse_levelorder"))
