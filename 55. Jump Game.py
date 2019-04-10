
def canJump(nums):
    if len(nums)<=1:
        return True
    length = len(nums) - 1
    count = nums[0]
    ptr = 0
    while count >= ptr and ptr <= length:
        count = max(count, nums[ptr] + ptr)
        if count>=length:
            break
        ptr += 1
    return count >= length