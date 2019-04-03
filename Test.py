class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    number = {'0': ' ', '1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
              '9': 'wxyz'}
    if len(digits) == 1:
        return number[digits]
    list = []
    rever(number, digits, 0, '', list)
    return list


def rever(number, digits, count, string, list):
    if count == len(digits):
        return
    if len(string).__eq__(len(digits)):
        list.append(string)
    print(number[digits[count]].split())
    for value in number[digits[count]].split():
        rever(number, digits, count + 1, string + value, list)


def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    list=[]
    for i in range(n):
        if i==0:
            list.append(1)
        elif i==1:
            list.append(2)
        else:
            list.append(list[i-1]+list[i-2])
    return list[n-1]
    # if n == 0:
    #     return 1
    # elif n < 0:
    #     return 0
    # return climbStairs(n - 1) + climbStairs(n - 2)


if __name__ == '__main__':
    print(climbStairs(6))
    l1 = ListNode(5)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(3)
    l1.next.next.next.next = ListNode(4)
    l1.next.next.next.next.next = ListNode(6)
    l1.next.next.next.next.next.next = ListNode(7)
    l1.next.next.next.next.next.next.next = ListNode(8)
