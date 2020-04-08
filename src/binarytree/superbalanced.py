class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


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