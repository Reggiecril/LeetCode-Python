def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if p == None or q == None:
        return q == p
    # return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    if p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return False
