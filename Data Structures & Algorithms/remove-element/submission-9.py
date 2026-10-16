class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        start = 0
        end = len(nums) - 1

        while start <= end:
            while start <= end and nums[start] != val:
                start += 1
            while start <= end and nums[end] == val:
                end -= 1
            if start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        return start
        