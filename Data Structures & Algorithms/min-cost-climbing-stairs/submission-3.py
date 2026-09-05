class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cache = {}

        def climbCost(i):

            if i >= len(cost):
                return 0 
            if i in cache:
                return cache[i]
            else:
                res =  cost[i] + min(climbCost(i+1), climbCost(i+2))
                cache[i] = res
                return res

        return min(climbCost(0), climbCost(1))
            
            
        