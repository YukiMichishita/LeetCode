from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        daily_robbable_amounts = [nums[0], max(nums[:2])]
        for i in range(2, len(nums)):
            include_i = daily_robbable_amounts[i - 2] + nums[i]
            exclude_i = daily_robbable_amounts[i - 1]
            daily_robbable_amounts.append(max(include_i, exclude_i))
        return daily_robbable_amounts[len(nums) - 1]
