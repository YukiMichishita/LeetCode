import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heapq = []
        for i in nums:
            self.add(i)

    def add(self, val: int) -> int:
        heapq.heappush(self.heapq, val)
        if len(self.heapq) > self.k:
            heapq.heappop(self.heapq)
        return self.heapq[0]
