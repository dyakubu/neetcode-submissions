"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return

        oldToNew = {}

        visited = set()

        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            oldToNew[node] = Node(node.val)
            for nei in node.neighbors:
                dfs(nei)

        dfs(node)

        for orig_node in oldToNew:
            clone = oldToNew[orig_node]
            for nei in orig_node.neighbors:
                clone.neighbors.append(oldToNew[nei])

        return oldToNew[node]
        
        