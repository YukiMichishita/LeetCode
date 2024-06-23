from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_robbable_amounts = [nums[0], max(nums[:2])]
        for i in range(2, len(nums)):
            include_i = max_robbable_amounts[i - 2] + nums[i]
            exclude_i = max_robbable_amounts[i - 1]
            max_robbable_amounts.append(max(include_i, exclude_i))
        return max_robbable_amounts[-1]
