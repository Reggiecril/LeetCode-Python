def levelOrderBottom(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if root == None:
        return list()
    a = [root]
    all = []
    while len(a) != 0:
        length = len(a)
        cur = []
        for i in range(length):
            temp = a[0]
            a.remove(temp)
            cur.append(temp.val)
            if temp.left != None:
                a.append(temp.left)
            if temp.right != None:
                a.append(temp.right)

        all.append(cur)

    return all[::-1]