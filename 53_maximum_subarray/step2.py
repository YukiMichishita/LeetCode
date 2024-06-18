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
        def calc_max_sub_array(head: int):
            if head >= len(nums) - 1:
                return nums[head]
            nonlocal max_sum
            next_max_prefix_array_sum = calc_max_sub_array(head + 1)
            max_prefix_array_sum = max(nums[head], next_max_prefix_array_sum + nums[head])
            max_sum = max(max_sum, max_prefix_array_sum)
            return max_prefix_array_sum
        max_sum = nums[-1]
        calc_max_sub_array(0)
        return max_sum


# kadane's algorithmを知らない場合に自力で思いつくとしたら累積和を使う解法になりそうだがO(n^2)でTimeoutする。
# 開始点をズラしながら累積和を取っていった時の最大値が回答。
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray_sum = nums[0]
        for i in range(len(nums)):
            cumulative_sum_from_i = 0
            for j in range(i, len(nums)):
                cumulative_sum_from_i += nums[j]
                max_subarray_sum = max(max_subarray_sum, cumulative_sum_from_i)
        return max_subarray_sum


# >i番目の累積和prefix_sum[i]を定義しておいてprefix_sum[i] - i番目より前のprefix_sumの最小値を計算して部分列和の最大値を更新していく方法もあります。Kadaneの前段階みたいな方法ですが
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = 0
        min_prefix_sum = 0
        max_subarray_sum = nums[0]
        for num in nums:
            min_prefix_sum = min(min_prefix_sum, prefix_sum)
            prefix_sum += num
            max_subarray_sum = max(max_subarray_sum, prefix_sum - min_prefix_sum)
        return max_subarray_sum
