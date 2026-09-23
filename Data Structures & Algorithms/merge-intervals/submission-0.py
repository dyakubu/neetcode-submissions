class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda i:i[0])
        mergedIntervals = []

        i = 0

        if len(intervals) <= 1:
            return intervals
        
        cur_start, cur_end = intervals[0]

        for i in range(1, len(intervals)):

            start, end = intervals[i]

            if (start >= cur_start and start <= cur_end) or (cur_start >= start and cur_start <= end):
                cur_start, cur_end = min(start, cur_start), max(end, cur_end)
            
            else:
                mergedIntervals.append([cur_start, cur_end])
                cur_start, cur_end = start, end

        mergedIntervals.append([cur_start, cur_end])

        return mergedIntervals
        