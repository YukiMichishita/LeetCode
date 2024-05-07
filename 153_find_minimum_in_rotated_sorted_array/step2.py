from typing import List

# step1を少し変更。
# left = -1にすることで[1,2,3]のように最初から昇順になっているパターンにも対応できるので、ループ前のチェックが不要になる
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = -1
        right = len(nums) - 1
        while left < right - 1:
            middle = (left + right) // 2
            if nums[left] < nums[middle]:
                left = middle
            if nums[middle] < nums[right]:
                right = middle
        return nums[right]


# left = rightで終わるパターン。直接最小値を探索しにいく。
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] < nums[right]:
                right = middle
            else:
                left = middle + 1
        return nums[left]


# 最小値を含む昇順の列を再帰的に探索するパターン。発想としては自然に思えるがコードにしてみるとそれほどわかりやすくもない？
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        middle = (left + right) // 2
        if nums[left] <= nums[right]:
            return nums[left]
        if nums[middle] < nums[right]:
            return self.findMin(nums[:middle + 1])
        return self.findMin(nums[middle + 1:])
