from typing import List

def find_duplicate_faster(nums:List[int]) -> int:
    head = nums[len(nums) - 1]
    left = head
    right = head
    for i in range(_find_cycle_length(nums)):
        right = nums[right - 1]
    while left != right:
        left = nums[left - 1]
        right = nums[right - 1]
    return left

def _find_cycle_length(nums:List[int]) -> int:
    current = len(nums) - 1
    l = len(nums)
    #get into the cycle
    while l > 0:
        current = nums[current - 1]
        l -= 1
    #at this point we are definitely in the cycle
    spot = current
    i = 1
    current = nums[current - 1]
    while spot != current:
        current = nums[current - 1]
        i += 1
    return i

    

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
    return l            

print(find_duplicate([1,2,3,6,2,5,4]))
print(find_duplicate_faster([1,2,3,6,2,5,4]))

print(find_duplicate([3,3,2,1]))
print(find_duplicate_faster([3,3,2,1]))

print(find_duplicate([3,2,1,1]))
print(find_duplicate_faster([3,2,1,1]))