from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_to_index = {}
        for i, n in enumerate(nums):
            if target - n in nums_to_index.keys():
                return [i, nums_to_index[target - n]]
            nums_to_index[n] = i

        return []
