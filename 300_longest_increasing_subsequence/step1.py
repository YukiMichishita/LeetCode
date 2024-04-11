from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # target以上の最小の要素のindexを返す
        def binary_search_insert_position(nums, target):
            left = 0
            right = len(nums) - 1
            while left < right:
                middle = (left + right) // 2
                if target > nums[middle]:
                    left = middle + 1
                else:
                    right = middle - 1
            if target > nums[left]:
                return left + 1
            return left

        min_tails_of_increasing_subsequences = [nums[0]]
        for num in nums:
            if num > min_tails_of_increasing_subsequences[-1]:
                min_tails_of_increasing_subsequences.append(num)
            else:
                i = binary_search_insert_position(min_tails_of_increasing_subsequences, num)
                min_tails_of_increasing_subsequences[i] = num

        return len(min_tails_of_increasing_subsequences)
