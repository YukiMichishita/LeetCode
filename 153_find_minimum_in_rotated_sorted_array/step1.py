from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 0回またはlen(nums)回ローテートされており昇順になっている場合
        if nums[0] < nums[-1]:
            return nums[0]
        # nums[i] < nums[i - 1]となっているようなi、つまり昇順が崩れている境界を探す
        # たとえば[3,4,5,1,2]であればi=3
        # ループ終了時にrightがこのようなiとなる
        left = 0
        right = len(nums) - 1
        while left < right - 1:
            middle = (left + right) // 2
            if nums[left] < nums[middle]:
                left = middle
            if nums[middle] < nums[right]:
                right = middle
        return nums[right]
