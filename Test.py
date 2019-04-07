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


def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    list = [[0 for i in range(n)] for i in range(n)]
    left = 0
    right = n
    top = 0
    bottom = n
    count = 0
    while count<n*n:
        for i in range(right-left):
            list[top][left+i] = count + 1
            count += 1
        top += 1
        for i in range(bottom-top):
            list[top+i][right-1] = count + 1
            count += 1
        right -= 1
        for i in range(right-left):
            list[bottom-1][right-i-1]=count+1
            count+=1
        bottom-=1
        for i in range(bottom-top):
            list[bottom-1-i][left]=count+1
            count+=1
        left+=1
    #
    # n -= 1
    for i in range(n):
        print(list[i], '\n')


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
    print(generateMatrix(10))
