from math import comb


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        num_right_moving = m - 1
        num_bottom_moving = n - 1
        return comb(num_right_moving + num_bottom_moving, num_bottom_moving)
