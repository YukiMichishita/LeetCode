from typing import List
from bisect import bisect_left, bisect_right


# step1
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_be_shipped(capacity):
            current_total = 0
            day_to_ship = 1
            for w in weights:
                if current_total + w > capacity:
                    day_to_ship += 1
                    current_total = 0
                current_total += w
            return day_to_ship <= days

        low = max(weights) - 1
        high = sum(weights)
        while low < high - 1:
            middle = (low + high) // 2
            if can_be_shipped(middle):
                high = middle
            else:
                low = middle
        return high

# bisect_left
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_be_shipped(capacity):
            current_total = 0
            day_to_ship = 1
            for w in weights:
                if current_total + w > capacity:
                    day_to_ship += 1
                    current_total = 0
                current_total += w
            return day_to_ship <= days

        capacities = range(max(weights), sum(weights) + 1)
        return capacities[bisect_left(capacities, True, key=can_be_shipped)]

# bisect_right
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_be_shipped(capacity):
            current_total = 0
            day_to_ship = 1
            for w in weights:
                if current_total + w > capacity:
                    day_to_ship += 1
                    current_total = 0
                current_total += w
            return day_to_ship <= days

        capacities = range(max(weights), sum(weights) + 1)
        return capacities[bisect_right(capacities, False, key=can_be_shipped)]


