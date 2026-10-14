class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Directed graph. You must trust nobody
        # Everybody must trust you 

        # For each person who trusts no one traverse entire graph to find out if they are trusted by all. 
        # Seems woefully inefficient

        trustGraph = {i:[[], 0] for i in range(1, n+1)} # adj list of people and who they trust

        print(trustGraph)

        for truster, trustee in trust:
            trustGraph[truster][0].append(trustee)
            trustGraph[trustee][1] += 1

        print(trustGraph)

        for truster in trustGraph:
            if trustGraph[truster][0] == [] and trustGraph[truster][1] == n-1: #n-1 because judge does not trust themself
                return truster
    
        return -1




