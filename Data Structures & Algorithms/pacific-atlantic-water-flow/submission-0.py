from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def find_reachable(q, visited):

            reachable = set(q)

            while q:

                r,c = q.popleft()

                if (r,c) in visited or r >= len(heights) or r < 0 or c >= len(heights[0]) or c < 0:
                    continue 

                visited.add((r,c))

                directions = [(0,1), (0,-1), (-1,0), (1,0)]

                for nr, nc in directions:
                    if r+nr < 0 or r+nr >= len(heights) or c+nc < 0 or c+nc >= len(heights[0]):
                        continue 
                    if heights[r+nr][c+nc] >= heights[r][c]:
                        reachable.add((r+nr,c+nc))
                        q.append((r+nr, c+nc))

            return reachable

        pacifiq = deque()
        atlantiq = deque()
        visited = set()

        for row in range(len(heights)):
            pacifiq.append((row, 0))

        for col in range(len(heights[0])):
            pacifiq.append((0, col))
        

        for col in range(len(heights[0])):
            atlantiq.append((len(heights)-1, col))

        for row in range(len(heights)):
            atlantiq.append((row, len(heights[0])-1))
     

        pacific = find_reachable(pacifiq, visited)
        visited.clear()
        atlantic = find_reachable(atlantiq, visited)

        return list(pacific & atlantic)
                



        