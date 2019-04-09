
################Before Optimize(32%)###############
def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    in_list = []
    out_list = []
    count = 0
    getSum(candidates, target, in_list, out_list, count)
    return out_list


def getSum(candidates, target, in_list, out_list, count):
    while count < len(candidates):
        if target < 0:
            return
        elif target == 0 and in_list not in out_list:
            out_list.append(in_list.copy())
            return
        else:
            in_list.append(candidates[count])
            getSum(candidates, target-candidates[count], in_list, out_list, count)
            in_list.pop()
            count += 1
################After Optimize (95%)###############
def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    in_list = []
    out_list = []
    getSum(sorted(candidates), target, in_list, out_list)
    return out_list


def getSum(candidates, target, in_list, out_list):
    if target == 0:
        out_list.append(in_list.copy())
        return
    for i in candidates:
        if target<i:
            break
        if in_list and in_list[-1]>i:continue
        else:
            in_list.append(i)
            getSum(candidates, target-i, in_list, out_list)
            in_list.pop()
