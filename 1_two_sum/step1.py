from typing import List


class Solution:
    def __init__(self):
        self.l = {}

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            self.l[n] = i

        for i, n in enumerate(nums):
            if (target-n) in self.l.keys() and i != self.l[target-n]:
                return [i, self.l[target - n]]

        return []
