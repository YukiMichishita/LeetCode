from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        OBSTACLE = 1
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        unique_paths_table = [[0] * width for _ in range(height)]
        if obstacleGrid[0][0] != OBSTACLE:
            unique_paths_table[0][0] = 1
        for row in range(height):
            for col in range(width):
                if obstacleGrid[row][col] == OBSTACLE:
                    continue
                if row > 0:
                    unique_paths_table[row][col] += unique_paths_table[row - 1][col]
                if col > 0:
                    unique_paths_table[row][col] += unique_paths_table[row][col - 1]
        return unique_paths_table[height - 1][width - 1]
