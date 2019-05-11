def mySqrt(self, x: int) -> int:
    left = 0
    right = x
    while left <= right:
        mid = int(left + (right - left) / 2)
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif mid * mid > x:
            right = mid
        else:
            left = mid + 1
    return mid