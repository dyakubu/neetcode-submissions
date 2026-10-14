from collections import deque
class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        INF = 2147483647
        numRows = len(grid)
        numCols = len(grid[0])

        sources = deque()
        visited = set()

        for row in range(numRows):   # sources = (0,2) (3,0)
            for col in range(numCols):
                if grid[row][col] == 0:
                    sources.append((row, col))

        while sources:
            sr, sc = sources.popleft() # sr, sc = 0, 2

            directions = [(1,0), (-1,0), (0,-1), (0,1)]

            for dx, dy in directions:

                if sr+dx >= numRows or sr+dx < 0 or sc+dy >= numCols or sc+dy < 0:
                    continue

                nei = grid[sr+dx][sc+dy]

                if nei == INF:       
                    grid[sr+dx][sc+dy] = grid[sr][sc] + 1
                    visited.add((sr+dx, sc+dy))  
                    sources.append((sr+dx, sc+dy))




        