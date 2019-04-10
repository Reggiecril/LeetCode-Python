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


def canJump(nums):
    if len(nums)<=1:
        return True
    length = len(nums) - 1
    count = nums[0]
    ptr = 0
    while count >= ptr and ptr <= length:
        count = max(count, nums[ptr] + ptr)
        if count>=length:
            break
        ptr += 1
    return count >= length


if __name__ == '__main__':
    print(canJump([3, 2, 1, 0, 4]))
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
