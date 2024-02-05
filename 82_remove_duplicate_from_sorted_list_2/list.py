from typing import List


class Solution:
    def deleteDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        i = 0
        val_to_remove = None
        while i < len(nums):
            if nums[i] == val_to_remove:
                i += 1
                continue
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                val_to_remove = nums[i]
                continue
            result.append(nums[i])
            i += 1
        return result


s = Solution()

case1 = [1, 2, 3, 3, 4, 4, 5]
expected1 = [1, 2, 5]
actual1 = s.deleteDuplicates(case1)
assert actual1 == expected1, f"case1 failed expected:{expected1}, actual:{actual1}"

case2 = [1, 1, 1, 2, 3]
expected2 = [2, 3]
actual2 = s.deleteDuplicates(case2)
assert actual2 == expected2, f"case2 failed expected:{expected2}, actual:{actual2}"
