from collections import defaultdict
class Solution:

    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adjList = {}

        for i in range(n):
            adjList[i] = []

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        if len(edges) != n-1:
            return False 

        visited = set()

        def dfs(node, parent):

            if node in visited:
                return 
            
            visited.add(node)

            for nei in adjList[node]:
                if node == parent:
                    continue 
                dfs(nei, node)

        dfs(0,-1)
        return len(visited) == n
        


        