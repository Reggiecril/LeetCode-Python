def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if strs == None or len(strs) == 0:
        return ""
    maxs = max(strs)
    mins = min(strs)
    s = ""
    for i in range(len(mins)):
        if mins[i] == maxs[i]:
            s += mins[i]
        else:
            return s
    return s

