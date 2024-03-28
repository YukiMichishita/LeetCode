from typing import List
import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_to_count = defaultdict(int)
        for n in nums:
            nums_to_count[n] += 1

        frequency_queue = []
        for num, frequency in nums_to_count.items():
            heapq.heappush(frequency_queue,(-frequency, num))

        top_k_frequent = []
        for _ in range(k):
            _, num = heapq.heappop(frequency_queue)
            top_k_frequent.append(num)

        return top_k_frequent

