def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if matrix==None or len(matrix)==0:
        return matrix
    list=[]

    left=0
    right=len(matrix[0])
    top=0
    bottom=len(matrix)
    count=right*bottom
    while True:
        for i in range(right-left):
            list.append(matrix[top][left+i])
            count-=1
        top += 1
        if count<=0:break
        for i in range(bottom-top):
            list.append(matrix[top+i][right-1])
            count-=1
        right -= 1
        if count <= 0: break
        for i in range(right-left):
            list.append(matrix[bottom-1][right-i-1])
            count-=1
        bottom-=1
        if count <= 0: break
        for i in range(bottom-top):
            list.append(matrix[bottom-1-i][left])
            count-=1
        left+=1
        if count <= 0: break
    return list
