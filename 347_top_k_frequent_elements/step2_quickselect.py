from typing import List, Tuple
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = defaultdict(int)
        for n in nums:
            num_to_count[n] += 1

        counts = list(num_to_count.items())

        def quick_select_top_k(target: List[Tuple[int, int]], top_k: int) -> List[Tuple[int,int]]:
            def median3(x, y, z):
                return max(min(x, y), min(max(x, y), z))

            def partition(target: List[Tuple[int, int]], left: int, right: int, pivot: int):
                while True:
                    while target[left][1] > pivot:
                        left += 1
                    while target[right][1] < pivot:
                        right -= 1
                    if left >= right:
                        return left - 1
                    target[left], target[right] = target[right], target[left]
                    left += 1
                    right -= 1

            def quick_sort_desc_top_k(target: List[Tuple[int, int]], left: int, right: int, top_k: int):
                if left == right:
                    return
                pivot = median3(target[left][1], target[right][1], target[left + (right - left + 1) // 2][1])
                p = partition(target, left, right, pivot)
                quick_sort_desc_top_k(target, left, p, top_k)
                if p < top_k:
                    quick_sort_desc_top_k(target, p + 1, right, top_k)

            quick_sort_desc_top_k(target, 0, len(target) - 1, top_k)
            return target[:top_k]

        top_k = quick_select_top_k(counts, k)
        return [k for (k, v) in top_k]
