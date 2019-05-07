def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    if nums == [] or len(nums) == 0:
        return []
    list = []
    self.permuteCal(nums, list, [], len(nums))
    return list


def permuteCal(self, nums, list, num_list, length):
    if len(num_list) == length and num_list not in list:
        list.append(num_list.copy())
        return
    for i in range(len(nums)):
        num_list.append(nums[i])
        new_num = nums.copy()
        new_num.pop(i)
        self.permuteCal(new_num, list, num_list, length)
        num_list.pop(-1)
    return