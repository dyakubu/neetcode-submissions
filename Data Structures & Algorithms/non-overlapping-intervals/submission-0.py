class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:


        nonOverlappingIntervals = []
        intervals.sort(key=lambda i: i[0])
        deletions = 0
        

        if len(intervals) <= 1:
            return 0

        cur_start, cur_end = intervals[0] 

        for i in range(1, len(intervals)):

            start, end = intervals[i]  

            # Overlapping intervals. Delete the one with later end time
            if (start >= cur_start and start < cur_end) or (cur_start >= start and cur_start < end):
                
                # Delete the one with the later end time
                if cur_end >= end:
                    cur_start, cur_end = start, end
                    deletions += 1

                else:
                    continue
            # Non-overlapping intervals. No deletions
            else:
                cur_start, cur_end = start, end
                nonOverlappingIntervals.append([cur_start, cur_end])
        nonOverlappingIntervals.append([cur_start, cur_end])
        return abs(len(nonOverlappingIntervals) - len(intervals))
        