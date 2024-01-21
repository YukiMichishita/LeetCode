from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heapq = nums
        heapq.heapify(self.heapq)

    def add(self, val: int) -> int:
        heapq.heappush(self.heapq, val)
        while len(self.heapq) > self.k:
            heapq.heappop(self.heapq)
        return self.heapq[0]
