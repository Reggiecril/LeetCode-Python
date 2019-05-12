def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    list = []
    for i in range(n):
        if i == 0:
            list.append(1)
        elif i == 1:
            list.append(2)
        else:
            list.append(list[i - 1] + list[i - 2])
    return list[n - 1]