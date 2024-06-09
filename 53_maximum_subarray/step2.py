from typing import List
from math import inf

# step1, kadane's algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = -inf
        for num in nums:
            current_sum = max(current_sum + num, num)
            max_sum = max(max_sum, current_sum)
        return max_sum


# 末尾ごとの部分配列の最大値を一旦リストにして、その最大値を求めるという2stepで考えたほうが自分が初見で理解するならわかりやすいと思った。
# 速度面では最後にmaxを取る分の差でstep1の方が有利。
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # max_suffix_array_sums[i] = 末尾がnums[i]となる部分配列の最大値
        max_suffix_array_sums = []
        max_suffix_sum = 0
        for num in nums:
            max_suffix_sum = max(max_suffix_sum + num, num)
            max_suffix_array_sums.append(max_suffix_sum)
        return max(max_suffix_array_sums)
            

# DPの遷移を再帰で考える方がわかりやすいかと思ったが、あまりわかりやすく書けなかった。
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def get_max_sub_array(head: int):
            if head >= len(nums) - 1:
                return nums[head], nums[head]
            next_max_sub_array_sum, next_max_prefix_array_sum = get_max_sub_array(head + 1)
            max_prefix_array_sum = max(nums[head], next_max_prefix_array_sum + nums[head])
            max_sub_array_sum = max(next_max_sub_array_sum, max_prefix_array_sum)
            return max_sub_array_sum, max_prefix_array_sum
        return get_max_sub_array(0)[0]


# kadane's algorithmを知らない場合に自力で思いつくとしたら累積和を使う解法になりそうだがO(n^2)でTimeoutする。
# 開始点をズラしながら累積和を取っていった時の最大値が回答。
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_array_sum = nums[0]
        for i in range(len(nums)):
            cumulative_sum_from_i = 0
            for j in range(i, len(nums)):
                cumulative_sum_from_i += nums[j]
                max_sub_array_sum = max(max_sub_array_sum, cumulative_sum_from_i)
        return max_sub_array_sum
