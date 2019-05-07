def permute(nums):
    out_list = []
    permuteCalculation([], out_list, nums, 0, len(nums))
    return out_list


def permuteCalculation(in_list, out_list, nums, count, length):
    if count == length:
        out_list.append(in_list.copy())
        return
    for i in nums:
        in_list.append(i)
        new_num=nums.copy()
        new_num.remove(i)
        permuteCalculation(in_list, out_list, new_num, count+1, length)
        in_list.pop(-1)
    return
