def myAtoi(str: str) -> int:
    if not str or len(str.lstrip())==0 or len(str)==0:
        return 0
    str = str.lstrip()
    minus = 1
    if str[0] == "-":
        str = str.replace("-", "", 1)
        minus = -1
    elif str[0] == "+":
        str = str.replace("+", "", 1)

        minus = 1
    dig=0
    for i in str:
        if not i.isdigit():
            return dig*minus
        dig=dig*10+int(i)
        if minus==1 and dig>2147483647:
            return 2147483647
        elif minus==-1 and dig>2147483648:
            return -2147483648
    return dig*minus