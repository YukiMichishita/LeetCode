from typing import List, Tuple
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums:List[int], k:int) -> List[int]:
        num_to_count = defaultdict(int)
        for n in nums:
            num_to_count[n] += 1

        counts = list(num_to_count.items())

        def quick_select_top_k(target:List[Tuple[int, int]], top_k:int) -> List[Tuple[int,int]]:
            def median3(x, y, z):
                return max(min(x, y), min(max(x, y), z))

            def quick_sort_desc_top_k(target:List[Tuple[int, int]], left:int, right:int, top_k:int) -> List[Tuple[int, int]]:
                print(target)
                if left == right:
                    return
                prev_left = left
                prev_right = right
                pivot = median3(target[left][1], target[right][1], target[left + (right - left) // 2][1])

                while True:
                    while target[left][1] > pivot:
                        left += 1
                    while target[right][1] < pivot:
                        right -= 1
                    if left > right:
                        if left <= top_k:
                            quick_sort_desc_top_k(target, prev_left, left - 1, top_k)
                        if top_k <= right:
                            quick_sort_desc_top_k(target, left, prev_right, top_k)
                    target[left], target[right] = target[right], target[left]
                    left += 1
                    right -= 1

            quick_sort_desc_top_k(target, 0, len(target) - 1, top_k)
            return target[:top_k]

        top_k = quick_select_top_k(counts, k)
        return [k for (k, v) in top_k]


s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2))
