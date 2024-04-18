from typing import List


class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        WATER = 0
        height = len(grid)
        width = len(grid[0])

        def calc_area(x: int, y: int) -> int:
            if not (width > x >= 0) or not (height > y >= 0) or visited[y][x] or grid[y][x] == WATER:
                return 0
            visited[y][x] = True
            return calc_area(x + 1, y) + calc_area(x - 1, y) + calc_area(x, y + 1) + calc_area(x, y - 1) + 1

        max_area = 0
        visited = [[False] * width for _ in range(height)]
        for y in range(height):
            for x in range(width):
                max_area = max(calc_area(x, y), max_area)

        return max_area

