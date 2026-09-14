"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key = lambda i:i.start)

        i = 0
        j = 1

        while j < len(intervals):
            if intervals[j].start < intervals[i].end:
                return False
            i += 1
            j += 1
        return True
        

        
