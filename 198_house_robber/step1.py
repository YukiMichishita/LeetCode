from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        daily_robbable_amounts = nums[:1]
        for i in range(1, len(nums)):
            num = nums[i]
            include_i = num
            if i >= 2:
                include_i += daily_robbable_amounts[i - 2]
            exclude_i = daily_robbable_amounts[i - 1]
            daily_robbable_amounts.append(max(include_i, exclude_i))
        return daily_robbable_amounts[len(nums) - 1]
