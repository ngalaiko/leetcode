from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_row = {}

        def max_in_row(row: int) -> int:
            if row in max_row:
                return max_row[row]

            max = grid[row][0]
            for i in range(1, len(grid)):
                if grid[row][i] > max:
                    max = grid[row][i]

            max_row[row] = max

            return max

        max_col = {}

        def max_in_column(col: int) -> int:
            if col in max_col:
                return max_col[col]

            max = grid[0][col]
            for i in range(1, len(grid)):
                if grid[i][col] > max:
                    max = grid[i][col]

            max_col[col] = max

            return max

        material = 0
        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                height = grid[row][col]
                material += min(max_in_row(row), max_in_column(col)) - height

        return material


if __name__ == '__main__':
    assert Solution().maxIncreaseKeepingSkyline(
        [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]) == 35
    assert Solution().maxIncreaseKeepingSkyline(
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0
