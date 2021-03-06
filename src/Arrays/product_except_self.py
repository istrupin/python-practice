from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left, right = [1] * length, [1] * length
        for i in range(1,length):
            left[i] = left[i-1] * nums[i-1]
        print(left)
        
        for j in range(length-1)[::-1]:
            right[j] = right[j+1] * nums[j+1]
        return [l * r for l,r in zip(left, right)]

    def productExceptSelf_constant_space(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1] * length
        for i in range(1,length):
            output[i] = output[i-1] * nums[i-1]
        prev = 1
        for j in range(length-1)[::-1]:
            output[j] *= prev * nums[j+1]
            prev *= nums[j+1]
        return output

    def productExceptSelfAgain(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        right =  nums[len(nums) - 1]
        for j in range(len(nums)-2, -1, -1):
            left[j] *= right
            right *= nums[j]
        return left


x = Solution()
# print(x.productExceptSelf_constant_space([1,3,7,4]))
print(x.productExceptSelfAgain([1,3,7,4]))