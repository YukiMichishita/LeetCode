from typing import List


# numsの中からtargetと等しい値を探し、複数ある場合は最も大きいindexを返す
def last_index(nums: List[int], target: int) -> int:
    return len(nums) - list(reversed(nums)).index(target) - 1


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        left_cursor = 0
        right_cursor = len(sorted_nums) - 1

        while left_cursor < right_cursor:
            left = sorted_nums[left_cursor]
            right = sorted_nums[right_cursor]
            if left + right == target:
                # nums = [3,3] target = 6のようなケースに備えて、大きい方のindexは逆順のリストから取る
                return [nums.index(left), last_index(nums, right)]
            elif left + right < target:
                left_cursor += 1
            else:
                right_cursor -= 1

        return []
