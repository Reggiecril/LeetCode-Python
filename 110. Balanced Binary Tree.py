#99.72%
def isBalanced(root):
    if not root:
        return True
    node,count=balanced(root,0)
    return node

def balanced(node: TreeNode, count: int):
    if not node:
        return True, count
    leftNode, left_dept = balanced(node.left, count)
    if not leftNode:
        return False, left_dept
    rightNode, right_dept = balanced(node.right, count)
    if not rightNode:
        return False, right_dept
    return abs(left_dept - right_dept) < 2,max(left_dept,right_dept)+1