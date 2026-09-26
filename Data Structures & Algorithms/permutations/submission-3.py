class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        permutations = []
        path = []
        used = [False] * len(nums)


        def findPermutations(): 

            if len(path) == len(nums):
                permutations.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                findPermutations()
                path.pop()
                used[i] = False

        findPermutations()
        return permutations
        