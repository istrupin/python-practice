from binarytree import BinaryTreeNode

def second_largest(root: BinaryTreeNode) -> BinaryTreeNode:
    node = root
    parent = root
    while node.right is not None:
        parent = node
        node = node.right
    if node.left is None:
        return parent
    else:
        node = node.left
        while node.right is not None:
            node = node.right
        return node

no_left_bst = BinaryTreeNode(5)
no_left_bst.insert_left(4)
no_left_bst.insert_right(6)
no_left_bst.right.insert_right(7)

print(second_largest(no_left_bst).value)

left_bst = BinaryTreeNode(5)
left_bst.left = BinaryTreeNode(3)
left_bst.right = BinaryTreeNode(8)
left_bst.right.left = BinaryTreeNode(7)
left_bst.right.right = BinaryTreeNode(12) #largest
left_bst.right.right.left = BinaryTreeNode(10) #left tree of largest
left_bst.right.right.left.left = BinaryTreeNode(9)
left_bst.right.right.left.right = BinaryTreeNode(11) #second largest

print(second_largest(left_bst).value)