def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    for i in range(len(s), 0, -1):
        for j in range(len(s) - i + 1):
            res = s[j:i + j]
            if res == res[::-1]:
                return res
    return ""