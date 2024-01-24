from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        num_of_zeros = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                num_of_zeros += 1
                nums.pop(i)
                continue
            i += 1
        nums += [0] * num_of_zeros
