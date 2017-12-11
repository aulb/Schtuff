# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        left, right = [], []
        start, end = newInterval.start, newInterval.end
        for interval in intervals:
            # If the current interval's end is less than the "start" it belong on the left side
            if interval.end < start:
                left.append(interval)
            # If the current interval's start is more than the end, it belong on the right side
            elif interval.start > end:
                right.append(interval)
            else:
                # merge the overlapping intervals, get new start and end
                start = min(start, interval.start)
                end = max(end, interval.end)
        return left + [Interval(start, end)] + right
    
        # # Assume non overlapping + non zero intervals
        # start, end = newInterval.start, newInterval.end
        # result = []
        # i = 0
        # while i < len(intervals): # Better to use while than for for things that potentially halts midway
        #     # Find candidate to merge
        #     if start <= intervals[i].end:
        #         if end < intervals[i].start:
        #             # Current interval is completely greater, time to append
        #             break
        #         # The end is still greater or equal to the current start, merge again
        #         start = min(start, intervals[i].start)
        #         end = max(end, intervals[i].end)
        #     else:
        #         # Otherwise if start > currentInterval's end, we need to merge later, just append to result
        #         result.append(intervals[i])
        #     i += 1
        # result.append(Interval(start, end))
        # result += intervals[i:] # Append the rest of the interval
        # return result
