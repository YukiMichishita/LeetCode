from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_suffix_array_sums = []
        max_suffix_sum = 0
        for num in nums:
            max_suffix_sum = max(max_suffix_sum + num, num)
            max_suffix_array_sums.append(max_suffix_sum)
        return max(max_suffix_array_sums)
