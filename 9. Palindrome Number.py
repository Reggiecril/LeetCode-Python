def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 10 and x > 0:
        return True
    x = str(x)
    length = len(x)
    count = 0
    while count < length / 2 + 1:
        first = x[count]
        last = x[length - 1 - count]
        if not first.__eq__(last):
            return False
        count += 1
    return True
###Best Solution
    # if str(x) == str(x)[::-1]:
    #     return True
    # else:
    #     return False


print(isPalindrome(123123123123123123123321321321321321321321))
