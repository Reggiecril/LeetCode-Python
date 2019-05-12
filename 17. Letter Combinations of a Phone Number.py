def letterCombinations(digits: str):
    mapper = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'qprs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    list=[""]
    for i in range(len(digits)):
        while len(list[0])==i:
            string=list.pop(0)
            for j in mapper[digits[i]]:
                list.append(j+string)
    return list