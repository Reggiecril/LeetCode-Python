def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    startPtr=0
    lastPtr=len(height)-1
    sum=0
    while lastPtr>startPtr:
        sum=max(sum,min(height[lastPtr],height[startPtr])*(lastPtr-startPtr))
        if height[lastPtr]>height[startPtr]:
            startPtr+=1
        elif height[startPtr]>height[lastPtr]:
            lastPtr-=1
        else:
            startPtr+=1
            lastPtr-=1
    return sum
print(maxArea([1,8,6,2,5,4,8,3,7]))