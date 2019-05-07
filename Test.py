class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# def rever(number, digits, count, string, list):
#     if count == len(digits):
#         return
#     if len(string).__eq__(len(digits)):
#         list.append(string)
#     print(number[digits[count]].split())
#     for value in number[digits[count]].split():
#         rever(number, digits, count + 1, string + value, list)
#

# def permute( nums):
#     out_list = []
#     permuteCalculation([], out_list, nums, 0, len(nums))
#     return out_list
#
#
# def permuteCalculation(in_list, out_list, nums, count, length):
#     if count == length:
#         out_list.append(in_list.copy())
#         return
#     for i in nums:
#         in_list.append(i)
#         new_num=nums.copy()
#         new_num.remove(i)
#         permuteCalculation(in_list, out_list, new_num, count+1, length)
#         in_list.pop()
#     return

def isSymmetric(root: TreeNode) -> bool:
    if root == None:
        return True
    return symmetric(root.left, root.right)


def symmetric(leftNode: TreeNode, rightNode: TreeNode):
    if leftNode == None or rightNode == None:
        return leftNode == rightNode
    if leftNode.val != rightNode.val:
        return False
    return symmetric(leftNode.left, rightNode.right) and symmetric(leftNode.right, rightNode.left)


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    # 50%
    # if s=='' or len(s)==0:
    #     return True;
    # l=[]
    # count=0
    # while count<len(s):
    #     if s[count]=='(' or s[count]=='[' or s[count]=='{':
    #         l.append(s[count])
    #     else:
    #         if len(l)==0:
    #             return False
    #         else:
    #             first=l[-1]
    #             second=s[count]
    #             if first=='(' and second==')' or first=='[' and second==']' or first=='{' and second=='}':
    #                 l.pop(-1)
    #             else:
    #                 return False
    #     count+=1
    # return len(l)==0
    # 100%
    stack = []
    for ch in s:
        if ch == "(":
            stack.append(")")
        elif ch == "{":
            stack.append("}")
        elif ch == "[":
            stack.append("]")
        else:
            if not stack: return False
            if stack[-1] != ch: return False
            stack.pop()
    return len(stack) == 0





if __name__ == '__main__':
    #     print(uniquePathsWithObstacles([
    #   [0,0,0],
    #   [0,1,0],
    #   [0,0,0]
    # ]))
    print(isValid("()[]{}"))
    l1 = ListNode(0)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(3)
    l1.next.next.next.next = ListNode(4)
    l1.next.next.next.next.next = ListNode(6)
    l1.next.next.next.next.next.next = ListNode(7)
    l1.next.next.next.next.next.next.next = ListNode(8)
    #
    # l3=ListNode(0)
    # l3.next=rotateRight(l1,2)
    # while l3:
    #     print(l3.val)
    #     l3=l3.next

    l1 = TreeNode(1)
    l1.left = TreeNode(2)
    l1.right = TreeNode(2)
    l1.right.left = TreeNode(3)
    l1.right.right = TreeNode(4)
    l1.left.left = TreeNode(4)
    l1.left.right = TreeNode(3)
    # l2 = TreeNode(1)
    # l2.left = TreeNode(2)
    # l2.right = TreeNode(3)
    # l2.right.left = TreeNode(5)
    # l2.right.left.left = TreeNode(5)

