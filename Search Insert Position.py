def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 1:
        return 0 if target <= nums[0] else 1
    if target > nums[len(nums) - 1]:
        return len(nums)
    elif target <= nums[0]:
        return 0
    for i in range(len(nums)):
        if target <= nums[i]:
            return i


print(searchInsert([1], 0))
