from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # zeroを後ろに送る = non-zeroを前に詰める と考える
        i = 0
        destination = 0
        while i < len(nums):
            while destination < len(nums) and nums[destination] != 0:
                destination += 1
            if nums[i] != 0 and destination < i:
                nums[i], nums[destination] = nums[destination], nums[i]
            i += 1
