from typing import List
from bisect import bisect_left

# 1. 一番シンプルな二分探索 探索範囲は[left, right]
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # target以上の最小の要素のindexを返す。戻り値をindexとすると、
        # 事後条件 : target <= nums[index] ∧ ∀x < index : nums[x] < target
        def binary_search_insert_position(nums, target):
            left = 0
            right = len(nums) - 1
            # 不変条件 : a ∧ b where
            # a) ∀x < left : nums[x] < target
            # b) ∀x > right : target <= nums[x]
            while left <= right:
                middle = (left + right) // 2
                if nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
            # ループが継続している間は left <= middle <= rightで, leftとrightは1ずつしか動かない
            # よって、この時点でleft = right + 1になっている
            # 不変条件のbとright = left - 1から、c)∀x > left - 1 : target <= nums[x]
            # c)のxにleftを代入して、target <= nums[left]
            # 不変条件のaと合わせて、leftが戻り値の条件を満たす
            return left

        increasing_subsequences = []
        for num in nums:
            if not increasing_subsequences or num > increasing_subsequences[-1]:
                increasing_subsequences.append(num)
            else:
                i = binary_search_insert_position(increasing_subsequences, num)
                increasing_subsequences[i] = num

        return len(increasing_subsequences)

# 1-2.探索範囲が[left, right]で、終了時にleft = rightになるバージョン
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binary_search_insert_position(nums, target):
            if not nums or nums[-1] < target:
                return len(nums)
            left = 0
            right = len(nums) - 1
            while left < right:
                middle = (left + right) // 2
                if nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle
            return left

        increasing_subsequences = []
        for num in nums:
            if not increasing_subsequences or num > increasing_subsequences[-1]:
                increasing_subsequences.append(num)
            else:
                i = binary_search_insert_position(increasing_subsequences, num)
                increasing_subsequences[i] = num

        return len(increasing_subsequences)


# 2. 1の二分探索に対して、途中で挿入箇所を見つけたらループを抜ける処理を追加。targetと同じ値がnumsの中にあるケースで少し速いはず。
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

        increasing_subsequences = []
        for num in nums:
            if not increasing_subsequences or num > increasing_subsequences[-1]:
                increasing_subsequences.append(num)
            else:
                i = binary_search_insert_position(increasing_subsequences, num)
                increasing_subsequences[i] = num

        return len(increasing_subsequences)


# 3. 探索範囲を[left, right)とする場合。2.のrightにright-1を代入したと考えられる。
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binary_search_insert_position(nums, target):
            left = 0
            right = len(nums)
            while left < right:
                middle = (left + right) // 2
                if nums[middle] == target:
                    return middle
                if nums[middle] < target:
                    left = middle + 1
                if target < nums[middle]:
                    right = middle
            return left

        increasing_subsequences = []
        for num in nums:
            if not increasing_subsequences or num > increasing_subsequences[-1]:
                increasing_subsequences.append(num)
            else:
                i = binary_search_insert_position(increasing_subsequences, num)
                increasing_subsequences[i] = num

        return len(increasing_subsequences)



# 3. Pythonの標準ライブラリにあるbisectを使う
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        increasing_subsequences = []
        for num in nums:
            if not increasing_subsequences or num > increasing_subsequences[-1]:
                increasing_subsequences.append(num)
            else:
                i = bisect_left(increasing_subsequences, num)
                increasing_subsequences[i] = num

        return len(increasing_subsequences)


# 4. 参考にした記事が二分探索していたのでstep1では二分探索してみたが、線形探索でもO(n^2)では解ける
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def linear_search_insert_position(nums, target):
            for i in range(len(nums)):
                if target <= nums[i]:
                    return i
            return len(target)

        increasing_subsequences = []
        for num in nums:
            if not increasing_subsequences or num > increasing_subsequences[-1]:
                increasing_subsequences.append(num)
            else:
                i = linear_search_insert_position(increasing_subsequences, num)
                increasing_subsequences[i] = num

        return len(increasing_subsequences)

