from binarytree import BinaryTreeNode

def isSuperBalanced(root: BinaryTreeNode) -> bool:
    #do dfs
    #maintain record of deepest and shallowest leaf
    #subtract deep - shallow and return true if difference > 1
    deepest, shallowest = None, None
    stack = []
    depth = 0
    stack.append((root, depth))
    while len(stack) != 0:
        node, depth = stack.pop()
        if isLeaf(node):
            if deepest is None and shallowest is None:
                deepest, shallowest = depth, depth
            if depth > deepest:  
                deepest = depth
            if depth < shallowest:
                shallowest = depth
            if (deepest - shallowest) > 1:
                return False
        if node.left is not None:
            stack.append((node.left, depth+1))
        if node.right is not None:
            stack.append((node.right, depth+1))
    return True

def isLeaf(node: BinaryTreeNode):
    return node.left is None and node.right is None

sb = BinaryTreeNode(1)
sb.left = BinaryTreeNode(2)
sb.right = BinaryTreeNode(3)

nb = BinaryTreeNode(1)
nb.left =BinaryTreeNode(2)
nb.right = BinaryTreeNode(3)
nb.left.left = BinaryTreeNode(4)
nb.left.left.left = BinaryTreeNode(5) 

print(isSuperBalanced(sb))