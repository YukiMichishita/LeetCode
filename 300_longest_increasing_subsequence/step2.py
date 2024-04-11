from typing import List


# 2分探索部分を35_search_insert_position.pyの書き方で書くと以下になるが、自分としてはstep1の方がわかりやすい
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binary_search_insert_position(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                middle = (left + right) // 2
                if nums[middle] == target:
                    return middle
                if nums[middle] < target:
                    left = middle + 1
                if target < nums[middle]:
                    right = middle - 1
            return left

        min_tails_of_increasing_subsequences = [nums[0]]
        for num in nums:
            if num > min_tails_of_increasing_subsequences[-1]:
                min_tails_of_increasing_subsequences.append(num)
            else:
                i = binary_search_insert_position(min_tails_of_increasing_subsequences, num)
                min_tails_of_increasing_subsequences[i] = num

        return len(min_tails_of_increasing_subsequences)


# 参考にした記事が二分探索していたのでstep1では二分探索してみたが、線形探索でもO(n^2)では解ける
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def linear_search_insert_position(nums, target):
            for i in range(len(nums)):
                if target <= nums[i]:
                    return i
            return len(target)

        min_tails_of_increasing_subsequences = [nums[0]]
        for num in nums:
            if num > min_tails_of_increasing_subsequences[-1]:
                min_tails_of_increasing_subsequences.append(num)
            else:
                i = linear_search_insert_position(min_tails_of_increasing_subsequences, num)
                min_tails_of_increasing_subsequences[i] = num

        return len(min_tails_of_increasing_subsequences)
