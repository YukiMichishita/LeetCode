import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heapq = []
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        heapq.heappush(self.heapq, val)
        if len(self.heapq) > self.k:
            heapq.heappop(self.heapq)
        return self.heapq[0]
