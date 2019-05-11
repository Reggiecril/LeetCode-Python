def pathSum(root: TreeNode, sum: int):
    all_list = []
    if not root:
        return list(all_list)
    suma(root, all_list, [], sum)
    return all_list


def suma(node, all_list, this_list, sum):
    if not node:
        return
    if sum - node.val == 0 and not node.left and not node.right:
        this_list.append(node.val)
        all_list.append(this_list.copy())
        this_list.pop()
        return
    else:
        this_list.append(node.val)
        suma(node.left, all_list, this_list, sum - node.val)
        suma(node.right, all_list, this_list, sum - node.val)
        this_list.pop()
        return