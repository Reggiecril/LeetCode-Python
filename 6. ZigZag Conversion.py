
def convert(s: str, numRows: int):
    if s == "" or numRows==1:
        return s
    l = ['']*numRows
    index, step = 0, 1
    for i in s:
        l[index] += i
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index += step
    return "".join(l)