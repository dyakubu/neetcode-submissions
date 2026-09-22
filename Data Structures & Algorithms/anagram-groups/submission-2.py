from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        groupedAnagrams = defaultdict(list)

        def charMap(s):

            freqs = [0] * 26
            for char in s:
                freqs[ord(char)-ord('a')] += 1
            return freqs
        
        for s in strs:
            charFreq = tuple(charMap(s))
            groupedAnagrams[charFreq].append(s)

        return [v for k, v in groupedAnagrams.items()]
