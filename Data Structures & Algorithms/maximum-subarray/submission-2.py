class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curSum = 0
        best = nums[0]


        for num in nums:
            curSum = max(curSum + num, num)
            best = max(best, curSum)

        return best
        