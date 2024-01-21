from typing import List
import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min = math.inf
        profit = 0
        for price in prices:
            if price < current_min:
                current_min = price
            if profit < price - current_min:
                profit = price - current_min

        return profit
