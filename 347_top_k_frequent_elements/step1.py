from typing import List
from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = defaultdict(int)
        for n in nums:
            num_to_count[n] += 1

        top_k = heapq.nlargest(k, num_to_count.items(), lambda item: item[1])
        return [int(num) for num, count in top_k]
