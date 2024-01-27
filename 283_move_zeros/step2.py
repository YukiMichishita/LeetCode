from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        first_zero = 0
        i = 0
        while i < len(nums):
            while first_zero < len(nums):
                if nums[first_zero] != 0:
                    first_zero += 1
                if nums[i] != 0 and first_zero < i:
                    nums[i], nums[first_zero] = nums[first_zero], nums[i]
                i += 1
