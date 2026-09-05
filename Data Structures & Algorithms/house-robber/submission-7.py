class Solution:
    def rob(self, nums: List[int]) -> int:

        cache = {}
        def Rob(i):
            

            if i >= len(nums):
                return 0 

            if i in cache:
                return cache[i]

            res = max(nums[i] + Rob(i+2), Rob(i+1))
            cache[i] = res 
            return res


        return max(Rob(0), Rob(1))

            
        