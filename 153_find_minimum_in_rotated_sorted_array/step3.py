from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = -1
        right = len(nums) - 1
        while left < right - 1:
            middle = (left + right) // 2
            if nums[left] < nums[middle]:
                left = middle
            if nums[middle] < nums[right]:
                right = middle
        return nums[right]
