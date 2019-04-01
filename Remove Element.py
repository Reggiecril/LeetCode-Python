def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    number = nums.count(val)
    if number != 0:
        while number > 0:
            nums.remove(val)
            number -= 1
    return len(nums)