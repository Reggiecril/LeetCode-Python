def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    p_list = []
    getParenthesis('', p_list, 0, 0, n);
    return p_list


def getParenthesis(string, p_list, o, c, n):
    if c == n:
        p_list.append(string)
    else:
        if o > c:
            getParenthesis(string + ')', p_list, o, c + 1, n)

        if o < n:
            getParenthesis(string + '(', p_list, o + 1, c, n)


print(generateParenthesis(3))
