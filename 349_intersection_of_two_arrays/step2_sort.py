from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sorted_nums1 = sorted(nums1)
        sorted_nums2 = sorted(nums2)
        intersection = set()
        i1 = 0
        i2 = 0

        while i1 < len(nums1) and i2 < len(nums2):
            if sorted_nums1[i1] == sorted_nums2[i2]:
                intersection.add(sorted_nums1[i1])
            if sorted_nums1[i1] <= sorted_nums2[i2]:
                i1 += 1
            else:
                i2 += 1

        return list(intersection)
