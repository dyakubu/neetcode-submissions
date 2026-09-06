class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {}
        def change(remaining):

            if remaining == 0:
                return 0

            if remaining < 0:
                return float('inf')

            if remaining in cache:
                return cache[remaining]

            fewest = float('inf')

            for coin in coins:
                fewest = min(fewest, 1+change(remaining-coin))
            cache[remaining] = fewest
            return fewest

        res = change(amount)
        if res == float('inf'):
            return -1
        return res
        