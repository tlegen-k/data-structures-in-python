from binary_search_tree import BST, Node
bst = BST(10)
bst.insert(3)
bst.insert(1)
bst.insert(25)
bst.insert(9)
bst.insert(13)

tree = BST(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(bst.search(9))
print(bst.search(14))

print(bst.is_bst_satisfied())
print(tree.is_bst_satisfied())
