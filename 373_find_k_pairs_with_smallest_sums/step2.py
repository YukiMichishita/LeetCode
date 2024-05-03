from typing import List
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        queue = []
        heapq.heappush(queue, (nums1[0] + nums2[0], 0, 0))
        visited = set()
        k_smallest_pairs = []

        def is_out_of_bounds(x, y):
            return x >= len(nums1) or 0 > x or y >= len(nums2) or 0 > y

        def is_visited(x, y):
            return (x, y) in visited

        def is_out_of_bounds_or_visited(x, y):
            return is_out_of_bounds(x, y) or is_visited(x, y)

        while k > 0:
            _, i, j = heapq.heappop(queue)
            k_smallest_pairs.append([nums1[i], nums2[j]])
            if not is_out_of_bounds_or_visited(i + 1, j) and is_out_of_bounds_or_visited(i + 1, j - 1):
                heapq.heappush(queue, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))
            if not is_out_of_bounds_or_visited(i, j + 1) and is_out_of_bounds_or_visited(i - 1, j + 1):
                heapq.heappush(queue, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))
            k -= 1

        return k_smallest_pairs
