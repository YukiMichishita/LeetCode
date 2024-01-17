from typing import List


# numsの中から、findingと一致する要素のindexのうち最大のものを返す。
def last_index(nums: List[int], finding: int) -> int:
    return len(nums) - list(reversed(nums)).index(finding) - 1


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        left_cursor = 0
        right_cursor = len(nums) - 1

        while left_cursor < right_cursor:
            left = sorted_nums[left_cursor]
            right = sorted_nums[right_cursor]
            two_sum = left + right

            if two_sum == target:
                # nums=[3,3] target=6のようなケースがあるため、2つめのindexはリスト後ろから見る
                return [nums.index(left), last_index(nums, right)]
            if two_sum < target:
                left_cursor += 1
            else:
                right_cursor -= 1

        return []
