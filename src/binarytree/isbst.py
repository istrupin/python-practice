from binarytree import BinaryTreeNode

def is_bst(root: BinaryTreeNode) -> bool:
    upper_bound = float('inf')
    lower_bound = -float('inf')
    return is_bst_helper(root, upper_bound, lower_bound)


def is_bst_helper(root: BinaryTreeNode, upper_bound: float, lower_bound: float) -> bool:
    if root is None:
        return True
    if root.value > lower_bound and root.value < upper_bound:
        return is_bst_helper(root.left, root.value, lower_bound) and is_bst_helper(root.right, upper_bound, root.value)
    return False


bst = BinaryTreeNode(5)
bst.insert_left(4)
bst.insert_right(6)
bst.right.insert_right(7)

print(is_bst(bst))

badBst = BinaryTreeNode(7)
badBst.insert_left(6)
badBst.insert_right(15)
badBst.left.insert_right(8) # bad value -- bigger than root

print(is_bst(badBst))