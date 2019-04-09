class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def rever(number, digits, count, string, list):
    if count == len(digits):
        return
    if len(string).__eq__(len(digits)):
        list.append(string)
    print(number[digits[count]].split())
    for value in number[digits[count]].split():
        rever(number, digits, count + 1, string + value, list)


def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    in_list = []
    out_list = []
    count = 0
    getSum(sorted(candidates), target, in_list, out_list)
    return out_list


def getSum(candidates, target, in_list, out_list):
    if target == 0:
        out_list.append(in_list.copy())
        return
    for i in candidates:
        if target<i:
            break
        if in_list and in_list[-1]>i:continue
        else:
            in_list.append(i)
            getSum(candidates, target-i, in_list, out_list)
            in_list.pop()
# def combinationSum(candidates, target):
#     """
#     :type candidates: List[int]
#     :type target: int
#     :rtype: List[List[int]]
#     """
#     in_list = []
#     out_list = []
#     count = 0
#     getSum(candidates, target, in_list, out_list, count)
#     return out_list
#
#
# def getSum(candidates, target, in_list, out_list, count):
#     while count < len(candidates):
#         if target < 0:
#             return
#         elif target == 0 and in_list not in out_list:
#             out_list.append(in_list.copy())
#             return
#         else:
#             in_list.append(candidates[count])
#             getSum(candidates, target-candidates[count], in_list, out_list, count)
#             in_list.pop()
#             count += 1

if __name__ == '__main__':
    # l1 = ListNode(5)
    # l1.next = ListNode(1)
    # l1.next.next = ListNode(2)
    # l1.next.next.next = ListNode(3)
    # l1.next.next.next.next = ListNode(4)
    # l1.next.next.next.next.next = ListNode(6)
    # l1.next.next.next.next.next.next = ListNode(7)
    # l1.next.next.next.next.next.next.next = ListNode(8)

    # l1 = TreeNode(2)
    # l1.left = TreeNode(2)
    # l1.right = TreeNode(3)
    # l1.right.right = TreeNode(3)
    # l1.right.right.right = TreeNode(3)
    l2 = TreeNode(1)
    l2.left = TreeNode(2)
    l2.right = TreeNode(3)
    l2.right.left = TreeNode(5)
    l2.right.left.left = TreeNode(5)
    print(combinationSum([2,3,6,7],7))
