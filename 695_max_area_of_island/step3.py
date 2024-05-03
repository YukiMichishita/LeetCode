from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        WATER = 0
        height = len(grid)
        width = len(grid[0])

        def calc_area(x, y):
            if not (0 <= x < width) or not (0 <= y < height) or visited[y][x] or grid[y][x] == WATER:
                return 0
            visited[y][x] = True
            return calc_area(x + 1, y) + calc_area(x, y + 1) + calc_area(x - 1, y) + calc_area(x, y - 1) + 1

        max_area = 0
        visited = [[False] * width for _ in range(height)]
        for x in range(width):
            for y in range(height):
                max_area = max(calc_area(x, y), max_area)

        return max_area
