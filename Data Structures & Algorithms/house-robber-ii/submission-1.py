class Solution:
    def rob(self, nums: List[int]) -> int:


        def Rob(arr, i, cache):

            if i >= len(arr):
                return 0 

            if i in cache:
                return cache[i]

            res = max(arr[i]+Rob(arr, i+2, cache), Rob(arr, i+1, cache))
            cache[i] = res
            return res

        if len(nums) == 1:
            return nums[0]
        f = nums[0:len(nums)-1]
        l = nums[1:len(nums)]


        rf = Rob(f, 0, {})
        rl = Rob(l, 0, {})

        return max(rf, rl)
        