from typing import List
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        queue = []
        for i, n in enumerate(nums2):
          heapq.heappush(queue, (nums1[0] + n, 0, i))
        k_smallest_pairs = []

        while k > 0 and queue:
          _, i, j = heapq.heappop(queue)
          k_smallest_pairs.append([nums1[i], nums2[j]])
          if i + 1 < len(nums1):
            heapq.heappush(queue, (nums1[i + 1] + nums2[j], i + 1, j))
          k -= 1

        return k_smallest_pairs
