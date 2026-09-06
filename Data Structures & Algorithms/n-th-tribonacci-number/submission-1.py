class Solution:
    def tribonacci(self, n: int) -> int:

        cache = {}
        def t(n):

            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1
            if n in cache:
                return cache[n]

            res = t(n-1) + t(n-2) + t(n-3)
            cache[n] = res
            return res

        return t(n)
        