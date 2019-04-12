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

def uniquePathsWithObstacles(obstacleGrid) -> int:
    m = len(obstacleGrid[0])
    n = len(obstacleGrid)
    value = 1
    for i in range(m):
        if obstacleGrid[0][i] == 1:
            value = 0
        obstacleGrid[0][i] = value
    value = 1
    for i in range(1, n):
        if obstacleGrid[i][0] == 1:
            value = 0
        obstacleGrid[i][0] = value
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[j][i] == 1:
                obstacleGrid[j][i] = 0
            else:
                obstacleGrid[j][i] = obstacleGrid[j - 1][i] + obstacleGrid[j][i - 1]

    return obstacleGrid[-1][-1]


def lengthOfLastWord(s: str) -> int:
    if len(s.strip())==0:
        return 0
    return s.strip().split(" ")[-1]


if __name__ == '__main__':
    #     print(uniquePathsWithObstacles([
    #   [0,0,0],
    #   [0,1,0],
    #   [0,0,0]
    # ]))
    str = 'Hello World!'
    print(lengthOfLastWord(str))
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

    # l1 = TreeNode(2)
    # l1.left = TreeNode(2)
    # l1.right = TreeNode(3)
    # l1.right.right = TreeNode(3)
    # # l1.right.right.right = TreeNode(3)
    # l2 = TreeNode(1)
    # l2.left = TreeNode(2)
    # l2.right = TreeNode(3)
    # l2.right.left = TreeNode(5)
    # l2.right.left.left = TreeNode(5)
