from typing import List


class Solution:
    def next_permutation(self, nums: List[int]) -> None:
        low, high = None, None
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                low = i
                break
        if low is None:
            nums.sort()
            return
        for h in range(i+1, len(nums)):
            print(f'h is {h}')
            if high is None or (nums[h] <= nums[high] and nums[h] > nums[low]):
                print(f'set high to {h}')
                high = h 
        print(low)
        print(high)
        print("###")
        #swap high and low
        temp = nums[high]
        nums[high] = nums[low]
        nums[low] = temp
        #reverse
        for j in range(low+1, (low+1 + len(nums))//2 ):
            comp = len(nums) - 1 - j + low + 1 
            temp = nums[comp]
            nums[comp] = nums[j]
            nums[j] = temp

x = Solution()
# inp = [2,3,1,3,3]
# inp = [1,2,1,1,3]
inp = [1,2,3]

x.next_permutation(inp)
print(inp)

