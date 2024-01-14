from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sorted_nums1 = sorted(nums1)
        sorted_nums2 = sorted(nums2)
        intersection = []
        i1 = 0
        i2 = 0

        while i1 < len(nums1) and i2 < len(nums2):
            if sorted_nums1[i1] < sorted_nums2[i2]:
                i1 += 1
                continue
            if sorted_nums2[i2] < sorted_nums1[i1]:
                i2 += 1
                continue

            tmp_cursor = sorted_nums1[i1]
            intersection.append(tmp_cursor)
            while i1 < len(nums1) and tmp_cursor == sorted_nums1[i1]:
                i1 += 1
            while i2 < len(nums2) and tmp_cursor == sorted_nums2[i2]:
                i2 += 1

        return intersection
