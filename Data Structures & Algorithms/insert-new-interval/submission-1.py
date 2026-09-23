class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        mergedIntervals = []

        cur_start, cur_end = newInterval

        for i, interval in enumerate(intervals):

            start, end = interval

            # No overlap. This interval definitely comes before cur. No interval update
            if cur_start > end:
                mergedIntervals.append([start, end])

            # Overlapping Intervals. Merge them
            elif (cur_start >= start and cur_start <= end) or (start >= cur_start and start <= cur_end):
                cur_start, cur_end = min(start, cur_start), max(end, cur_end)

            # No overlap. Update cur
            else:
                mergedIntervals.append([cur_start, cur_end])
                cur_start, cur_end = start, end
                
        mergedIntervals.append([cur_start, cur_end])
        return mergedIntervals


                


        