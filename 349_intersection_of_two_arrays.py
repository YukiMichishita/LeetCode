from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = set([])
        set1 = set(nums1)

        for n in nums2:
            if n in set1:
                answer.add(n)

        return list(answer)
