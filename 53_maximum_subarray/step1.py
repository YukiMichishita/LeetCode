from typing import List
from math import inf

# 解法がわからなかったので答えを見た
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = -inf
        for num in nums:
            current_sum = max(current_sum + num, num)
            max_sum = max(max_sum, current_sum)
        return max_sum
