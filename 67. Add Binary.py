def addBinary(self, a: str, b: str) -> str:
    s = ""
    count = 0
    i = len(a) - 1
    j = len(b) - 1
    while count >= 1 or i >= 0 or j >= 0:
        count += int(a[i]) if i >= 0 else 0
        i -= 1
        count += int(b[j]) if j >= 0 else 0
        j -= 1
        s = str(int(count % 2)) + s
        count /= 2

    return s