from typing import List


class Solution:
    def __init__(self):
        self.l = {}

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            if (target - n) in self.l.keys():
                return [i, self.l[target - n]]
            self.l[n] = i

        return []
