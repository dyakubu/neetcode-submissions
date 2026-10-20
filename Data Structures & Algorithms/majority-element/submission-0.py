class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        cur = None
        count = 0
        
        for num in nums:
            if num == cur:
                count += 1
            elif count == 0:
                cur = num
                count = 1
            else:
                count -= 1

        return cur if cur is not None else nums[0]


        


        