def minDepth(self, root: TreeNode) -> int:
    if root == None:
        return 0
    return self.min(root) + 1


def min(self, root):
    if root.left == None and root.right == None:
        return 0
    elif root.left == None:
        return self.min(root.right) + 1
    elif root.right == None:
        return self.min(root.left) + 1
    else:
        return min(self.min(root.right), self.min(root.left)) + 1
