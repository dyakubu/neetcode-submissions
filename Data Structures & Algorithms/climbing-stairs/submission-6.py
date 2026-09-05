class Solution:
    def climbStairs(self, n: int) -> int:

        cache = {}

        def climb(n):
            if n == 0:
                return 1

            if n == 1:
                return 1
            
            if n in cache:
                return cache[n]

            else:
                res = climb(n-1) + climb(n-2)
                cache[n] = res 
                return res    

        return climb(n)