import collections
from typing import Tuple, List


def search(nums: List[int], target: int) -> int:
    if nums is None or len(nums) == 0:
        return -1
    if len(nums) == 1:
        return 0 if nums[0] == target else -1
    pivot = find_pivot(nums)
    left, right, mid = 0, len(nums) - 1, pivot

    while(left < right):
        print(f'left: {left} right: {right} mid: {mid}')
        if nums[mid] == target:
            return mid
        if mid != left and nums[left] <= target and target <= nums[mid-1]:
            right = mid - 1
        else:
            left = mid + 1
        mid = left + (right - left) // 2

    return mid if nums[mid] == target else -1

def find_pivot(arr: List[int]) -> int:
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return arr[0] 
    left, right, mid = _left_right_mid(arr)
    while left < right:
        if mid != 0 and arr[mid - 1] > arr[mid]: 
            return mid
        if arr[mid] > arr[right] and left != mid:
            left = mid
        else:
            right = mid - 1
        mid = left + (right - left) // 2         

    return left

def _left_right_mid(nums: List[int]) -> Tuple[int, int, int]:
    left, right = 0, len(nums) - 1
    mid = left + (right - left) // 2
    return (left, right, mid)

# p = search([4,5,6,7,0,1,2],2)
p = search([3,1],0)
print(p)
        