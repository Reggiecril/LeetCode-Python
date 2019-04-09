def singleNumber(nums):
    return sum(set(nums))*2-sum(nums)