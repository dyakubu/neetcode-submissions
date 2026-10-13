class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda i:i[0])
        merged = []
        cs, ce = intervals[0]

        for i_s, i_e in intervals[1:]:
            if (cs >= i_s and cs <= i_e) or (i_s >= cs and i_s <= ce):
                cs, ce = min(cs, i_s), max(ce, i_e)
            else:
                merged.append([cs, ce])
                cs, ce = i_s, i_e
        merged.append([cs, ce])

        return merged



        