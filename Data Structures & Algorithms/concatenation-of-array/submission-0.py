class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) * 2
        s1 = 0
        s2 = len(nums) 

        for num in nums:
            ans[s1] = num
            ans[s2] = num
            s1 += 1
            s2 += 1
        return ans
        