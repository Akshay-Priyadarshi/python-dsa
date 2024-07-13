def get_square_root(num: int):
    low = 1
    high = num - 1
    while low <= high:
        mid = low + (high - low) // 2
        mid_sq = mid * mid 
        if mid_sq == num:
            return mid
        elif mid_sq < num:
            low = mid + 1
        else:
            high = mid - 1
    return -1
