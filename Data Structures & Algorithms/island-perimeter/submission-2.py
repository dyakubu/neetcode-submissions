class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:


        def _islandPerimeter(i, j):

            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0:
                return 1
            if grid[i][j] == 0:
                return 1
            if grid[i][j] == 'X':
                return 0
            grid[i][j] = 'X'
            return _islandPerimeter(i+1, j) + _islandPerimeter(i-1,j) + _islandPerimeter(i, j+1) + _islandPerimeter(i, j-1)


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return _islandPerimeter(row,col)

        return 1
        