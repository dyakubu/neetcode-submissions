class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        longest = strs[0]

        if len(strs) == 1:
            return strs[0]

        longestSeen = strs[0]

        for word in strs:
            idx = 0
            l = 0
            while idx < len(word) and l < len(longestSeen):
                if word[idx] != longestSeen[l]:
                    break 
                idx += 1
                l += 1
            if idx == 0:
                return ""
            longest = longest[0:idx]

        return longest
                


        
        