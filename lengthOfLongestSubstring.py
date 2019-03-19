def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    collect = []
    length = 0
    for i in s:
        if i in collect:
            collect = collect[collect.index(i)+1:]
            collect.append(i)
        else:
            collect.append(i)
        length=max(len(collect),length)


print(lengthOfLongestSubstring("adv"))
