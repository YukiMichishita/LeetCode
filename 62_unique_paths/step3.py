class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_unique_paths_table = [[1] * n for _ in range(m)]
        for row in range(1, m):
            for column in range(1, n):
                num_unique_paths_table[row][column] = \
                    num_unique_paths_table[row - 1][column] + num_unique_paths_table[row][column - 1]
        return num_unique_paths_table[m - 1][n - 1]
