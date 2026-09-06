class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {}

        def minCoins(remaining):


            if remaining == 0:
                return 0

            if remaining < 0:
                return float('inf')

            if remaining in cache:
                return cache[remaining]


            best = float('inf')

            for coin in coins:
                 best = min(best, 1 + minCoins(remaining - coin))
                 cache[remaining] = best

            return best

        result = minCoins(amount)

        return -1 if result == float('inf') else result
        