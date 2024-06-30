from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        width = len(grid[0])
        height = len(grid)
        visited = [[False] * width for _ in range(height)]
        num_of_islands = 0

        def make_visited(x: int, y: int):
            if x >= width or 0 > x or y >= height or 0 > y or grid[y][x] == "0" or visited[y][x]:
                return
            visited[y][x] = True
            make_visited(x + 1, y)
            make_visited(x - 1, y)
            make_visited(x, y + 1)
            make_visited(x, y - 1)

        for y in range(height):
            for x in range(width):
                if grid[y][x] == "1" and not visited[y][x]:
                    num_of_islands += 1
                    make_visited(x, y)
                    visited[y][x] = True

        return num_of_islands
