from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (right + left) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                left = middle + 1
                continue
            if target < nums[middle]:
                right = middle - 1
                continue

        return left
