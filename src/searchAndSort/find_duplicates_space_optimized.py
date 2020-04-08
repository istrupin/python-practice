from typing import List

def find_duplicate(nums:List[int]) -> int:
    l = 1
    r = len(nums) 
    mid = len(nums)//2
    low_floor = 1
    low_ceil = mid
    while l < r:
        low_count, high_count = 0, 0
        mid = l + (r - l) // 2
        low_ceil = mid
        for n in nums:
            if n >= low_floor and n <= low_ceil:
                low_count += 1
            else:
                high_count += 1
        if low_count > low_ceil:
            r = mid 
        else:
            l = mid + 1
    return l-1            

print(find_duplicate([1,2,3,4,2,5,4]))