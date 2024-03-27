from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        cache = {}

        def moves(row: int, col: int) -> int:
            if col == len(grid[0]) - 1:
                return 0

            if row in cache and col in cache[row]:
                return cache[row][col]

            possible = [0]

            if row > 0 and grid[row][col] < grid[row-1][col+1]:
                possible.append(1 + moves(row-1, col+1))

            if grid[row][col] < grid[row][col+1]:
                possible.append(1 + moves(row, col+1))

            if row < len(grid)-1 and grid[row][col] < grid[row+1][col+1]:
                possible.append(1 + moves(row+1, col+1))

            if row in cache:
                cache[row][col] = max(possible)
            else:
                cache[row] = {}
                cache[row][col] = max(possible)

            return cache[row][col]

        return max([moves(row, 0) for row in range(len(grid))])


if __name__ == '__main__':
    assert Solution().maxMoves(
        [[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]) == 3
    assert Solution().maxMoves([[3, 2, 4], [2, 1, 9], [1, 1, 7]]) == 0
