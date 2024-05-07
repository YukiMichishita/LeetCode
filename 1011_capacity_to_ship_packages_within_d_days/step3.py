from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_be_shipped(capacity):
            current_total_weight = 0
            days_to_ship = 1
            for w in weights:
                if current_total_weight + w > capacity:
                    current_total_weight = 0
                    days_to_ship += 1
                current_total_weight += w
            return days_to_ship <= days

        low = max(weights) - 1
        high = sum(weights)
        while low < high - 1:
            middle = (low + high) // 2
            if can_be_shipped(middle):
                high = middle
            else:
                low = middle
        return high
        
