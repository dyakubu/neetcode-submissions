class Solution:

    def countSubstrings(self, s: str) -> int:


        def expand(left, right):

            count = 0

            while left >= 0 and right < len(s) and left <= right:

                if s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
                else:
                    break
            return count

        total = 0
        for i in range(len(s)):
            total += expand(i, i) + expand(i, i+1)

        return total



        