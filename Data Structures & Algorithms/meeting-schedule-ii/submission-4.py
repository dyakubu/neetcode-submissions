"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# [1,6] [2,4], [5,9] [12, 15], [17, 19]

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if len(intervals) <= 1:
            return len(intervals)

        intervals.sort(key=lambda i:i.start)

        heap = []
        first = intervals[0]
        heapq.heappush(heap, (first.end, first.start))

        minRooms = 1

        for i in range(1, len(intervals)):

            start, end = intervals[i].start, intervals[i].end
            e_end, e_start = heapq.heappop(heap)

            # can reuse same room. 
            if start >= e_end:
                heapq.heappush(heap, (end, start))
            
            else:
                heapq.heappush(heap, (e_end, e_start))
                heapq.heappush(heap, (end, start))
                minRooms += 1


        return minRooms


        