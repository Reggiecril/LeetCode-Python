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

def addBinary(a: str, b: str) -> str:
    s = ""
    count = 0
    i = len(a) - 1
    j = len(b) - 1
    while count >= 1 or i >= 0 or j >= 0:
        count += int(a[i]) if i >= 0 else 0
        i -= 1
        count += int(b[j]) if j >= 0 else 0
        j -= 1
        s = str(int(count % 2)) + s
        count /= 2

    return s


def convert(s: str, numRows: int):
    if s == "" or numRows==1:
        return s
    l = ['']*numRows
    index, step = 0, 1
    for i in s:
        l[index] += i
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index += step
    return "".join(l)

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
    print(convert("PAYPALISHIRING", 1))
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
