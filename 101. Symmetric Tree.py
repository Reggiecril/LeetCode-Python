def isSymmetric(root: TreeNode) -> bool:
    if root == None:
        return True
    return symmetric(root.left, root.right)


def symmetric(leftNode: TreeNode, rightNode: TreeNode):
    if leftNode == None or rightNode == None:
        return leftNode==rightNode
    if leftNode.val != rightNode.val:
        return False
    return symmetric(leftNode.left, rightNode.right) and symmetric(leftNode.right, rightNode.left)
