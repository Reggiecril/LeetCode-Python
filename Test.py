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

def strStr(haystack: str, needle: str) -> int:
    if haystack == "" or len(haystack) == 0 or needle == "" or len(needle) == 0:
        return -1
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:len(needle)+i]==needle:
            return i
    return -1

if __name__ == '__main__':
    #     print(uniquePathsWithObstacles([
    #   [0,0,0],
    #   [0,1,0],
    #   [0,0,0]
    # ]))

    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(1)
    l1.next.next.next = ListNode(1)
    l1.next.next.next.next = ListNode(1)
    l1.next.next.next.next.next = ListNode(6)
    l1.next.next.next.next.next.next = ListNode(7)
    l1.next.next.next.next.next.next.next = ListNode(8)
    print(strStr("aaab","ab"))
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
