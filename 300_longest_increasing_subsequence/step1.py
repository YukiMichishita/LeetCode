from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # target以上の最小の要素のindexを返す
        def binary_search_insert_position(nums, target):
            left = 0
            right = len(nums) - 1
            while left < right:
                middle = (left + right) // 2
                if nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
            if nums[left] < target:
                return left + 1
            return left

        increasing_subsequences = [nums[0]]
        for num in nums:
            if num > increasing_subsequences[-1]:
                increasing_subsequences.append(num)
            else:
                i = binary_search_insert_position(increasing_subsequences, num)
                increasing_subsequences[i] = num

        return len(increasing_subsequences)
