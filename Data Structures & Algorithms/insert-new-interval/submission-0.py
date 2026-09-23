class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        nstart, nend = newInterval

        mergedIntervals = []

        for i, interval in enumerate(intervals):

            start, end = interval 

            if nstart > end:  
                mergedIntervals.append([start, end])

            # Overlapping. Merge
            elif (nstart >= start and nstart <= end) or (start >= nstart and start <= nend):
                nstart = min(nstart, start)
                nend = max(end, nend)

            else:
                mergedIntervals.append([nstart, nend])
                nstart, nend = start, end

        mergedIntervals.append([nstart, nend])
        return mergedIntervals

        