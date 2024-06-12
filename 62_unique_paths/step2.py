from math import comb


# step1
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        num_right_moving = m - 1
        num_down_moving = n - 1
        return comb(num_right_moving + num_down_moving, num_down_moving)


# 問題カテゴリがDPなので想定解はこれかと思われる
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_unique_paths_table = [[1] * n for _ in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                num_unique_paths_table[row][col] = num_unique_paths_table[row][col - 1] \
                                                      + num_unique_paths_table[row - 1][col]
        return num_unique_paths_table[m - 1][n - 1]


# 空間計算量をO(m)にする。DPテーブルを潰して1列分だけ保持するイメージ。
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_unique_paths = [1] * m
        for col in range(1, n):
            for row in range(1, m):
                num_unique_paths[row] += num_unique_paths[row - 1]
        return num_unique_paths[m - 1]


# cacheを使ってcombinationを高速化
from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def combination(n: int, k: int):
            if n == 0 or k == 0 or n == k:
                return 1
            return combination(n - 1, k) + combination(n - 1, k - 1)
        num_right_moving = m - 1
        num_down_moving = n - 1
        return combination(num_right_moving + num_down_moving, min(num_right_moving, num_down_moving))
