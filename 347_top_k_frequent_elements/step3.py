from typing import List
from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_to_count = defaultdict(int)
        for n in nums:
            nums_to_count[n] += 1
        top_k = heapq.nlargest(k, nums_to_count.items(), lambda x: x[1])
        return [int(num) for num, _ in top_k]
