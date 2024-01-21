from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        sorted_nums1 = sorted(nums1)
        sorted_nums2 = sorted(nums2)
        index1 = 0
        index2 = 0

        while index1 < len(nums1) and index2 < len(nums2):
            num1 = sorted_nums1[index1]
            num2 = sorted_nums2[index2]
            if num1 < num2:
                index1 += 1
                continue
            if num2 < num1:
                index2 += 1
                continue

            common_num = num1
            intersection.append(common_num)
            while index1 < len(nums1) and sorted_nums1[index1] == common_num:
                index1 += 1
            while index2 < len(nums2) and sorted_nums2[index2] == common_num:
                index2 += 1

        return intersection
