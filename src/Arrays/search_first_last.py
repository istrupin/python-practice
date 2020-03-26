from typing import List

def search_range(nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        mid = left + (right - left) // 2
        

        while left <= right:
            if nums[mid] == target:
                return _get_range(nums, mid)
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            mid = left + (right - left) // 2

        return _get_range(nums, mid) if nums[mid] == target else [-1, -1]


def _get_range(nums: List[int], target: int) -> List[int]:
    left, right = target, target
    while left != 0 and nums[left-1] == nums[target]:
        left-=1
    while right != len(nums)-1 and nums[right+1] == nums[target]:
        right+=1
    return [left, right]


r = search_range([2,3],3)
print(r)
    
