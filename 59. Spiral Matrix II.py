def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    list = [[0 for i in range(n)] for i in range(n)]
    left = 0
    right = n
    top = 0
    bottom = n
    count = 0
    while count<n*n:
        for i in range(right-left):
            list[top][left+i] = count + 1
            count += 1
        top += 1
        for i in range(bottom-top):
            list[top+i][right-1] = count + 1
            count += 1
        right -= 1
        for i in range(right-left):
            list[bottom-1][right-i-1]=count+1
            count+=1
        bottom-=1
        for i in range(bottom-top):
            list[bottom-1-i][left]=count+1
            count+=1
        left+=1
    #
    # n -= 1
    for i in range(n):
        print(list[i], '\n')