def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root == None:
        return 0
    return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    # if root.left == None and root.right == None:
    #     return 1
    # elif root.left == None and root.right != None:
    #     return self.maxDepth(root.right) + 1
    # elif root.right == None and root.left != None:
    #     return self.maxDepth(root.left) + 1
    # else:
    #     return max(self.maxDepth(root.left),self.maxDepth(root.right))+1