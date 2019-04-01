def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    number = nums.count(val)
    if number != 0:
        sorted(nums)
        while number > 0:
            nums.remove(val)
            number -= 1
    return len(nums)


print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
