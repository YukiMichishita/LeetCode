from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        unique_paths_table = [[1] * width for _ in range(height)]
        for row in range(height):
            for col in range(width):
                if obstacleGrid[row][col] == 1:
                    unique_paths_table[row][col] = 0
                    continue
                if row == 0 and col == 0:
                    continue
                top = 0
                if row > 0:
                    top = unique_paths_table[row - 1][col]
                left = 0
                if col > 0:
                    left = unique_paths_table[row][col - 1]
                unique_paths_table[row][col] = top + left
        return unique_paths_table[height - 1][width - 1]
