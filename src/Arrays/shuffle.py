from typing import List
from random import randint

def shuffle(nums:List[int]) -> None:
    for i in range(len(nums)-1):
        swap_with = randint(i, len(nums)-1)
        if swap_with != i:
            nums[swap_with], nums[i] = nums[i], nums[swap_with]
    

nums = [1,2,3,4,5]
shuffle(nums)
print(nums)
