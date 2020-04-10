from binarytree import BinaryTreeNode

def isSuperBalanced(root: BinaryTreeNode) -> bool:
    return True

sb = BinaryTreeNode(1)
sb.left = BinaryTreeNode(2)
sb.right = BinaryTreeNode(3)

nb = BinaryTreeNode(1)
nb.left =BinaryTreeNode(2)
nb.right = BinaryTreeNode(3)
nb.left.left = BinaryTreeNode(4)
nb.left.left.left = BinaryTreeNode(5) 