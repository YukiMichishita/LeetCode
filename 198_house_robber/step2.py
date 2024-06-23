from typing import List

# len(nums) <= 2の時とi = 1あたりをどう処理するかで人により好みがありそう

# 例外的なケースに対する記述を最小限にした場合。
# len(nums) == 1の時にmax_robbable_amountsの長さが2になるのは直感に反するので、最初にearly returnした方がよいかもしれない。
class Solution:
    def rob(self, nums: List[int]) -> int:
        max_robbable_amounts = [nums[0], max(nums[:2])]
        for i in range(2, len(nums)):
            include_i = max_robbable_amounts[i - 2] + nums[i]
            exclude_i = max_robbable_amounts[i - 1]
            max_robbable_amounts.append(max(include_i, exclude_i))
        return max_robbable_amounts[-1]

# 空間計算量O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        max_2_days_ago = nums[0]
        max_1_day_ago = max(nums[:2])
        max_robbable = max_1_day_ago
        for num in nums[2:]:
            max_robbable = max(max_2_days_ago + num, max_1_day_ago)
            max_2_days_ago = max(max_2_days_ago, max_1_day_ago)
            max_1_day_ago = max_robbable
        return max_robbable
