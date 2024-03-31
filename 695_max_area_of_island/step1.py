from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        width = len(grid[0])
        height = len(grid)

        def calc_area(x: int, y: int) -> int:
            if grid[y][x] == 0:
                return 0
            area = 0
            visited = [[False] * width for _ in range(height)]

            def search_land(x: int, y: int):
                if x >= width or 0 > x or y >= height or 0 > y or visited[y][x] or grid[y][x] == 0:
                    return
                nonlocal area
                area += 1
                visited[y][x] = True
                search_land(x + 1, y)
                search_land(x - 1, y)
                search_land(x, y + 1)
                search_land(x, y - 1)

            search_land(x, y)
            return area

        max_area = 0
        for y in range(height):
            for x in range(width):
                max_area = max(calc_area(x, y), max_area)

        return max_area

