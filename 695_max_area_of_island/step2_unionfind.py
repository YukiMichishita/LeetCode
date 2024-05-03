from typing import List
from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, target):
        if self.parents[target] == target:
            return target
        # 経路圧縮
        self.parents[target] = self.find(self.parents[target])
        return self.parents[target]

    def union(self, target1, target2):
        parent1 = self.find(target1)
        parent2 = self.find(target2)
        if parent1 == parent2:
            return
        self.parents[parent2] = parent1

    def are_same_group(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        LAND = 1
        height = len(grid)
        width = len(grid[0])
        uf = UnionFind(width * height)

        def to_1d(x, y):
            return width * y + x

        def union_connected_lands(x, y):
            def is_land(x, y):
                return 0 <= x < width and 0 <= y < height and grid[y][x] == LAND

            if is_land(x + 1, y) and not uf.are_same_group(to_1d(x, y), to_1d(x + 1, y)):
                uf.union(to_1d(x, y), to_1d(x + 1, y))
                union_connected_lands(x + 1, y)
            if is_land(x, y + 1) and not uf.are_same_group(to_1d(x, y), to_1d(x, y + 1)):
                uf.union(to_1d(x, y), to_1d(x, y + 1))
                union_connected_lands(x, y + 1)

        for y in range(height):
            for x in range(width):
                if grid[y][x] == LAND and uf.find(to_1d(x, y)) == to_1d(x, y):
                    union_connected_lands(x, y)

        areas = defaultdict(int)
        for y in range(height):
            for x in range(width):
                if grid[y][x] == LAND:
                    areas[uf.find(to_1d(x, y))] += 1

        return max(areas.values(), default=0)
