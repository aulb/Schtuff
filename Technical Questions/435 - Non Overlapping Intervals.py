# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        """
        How come greedy works? Proof for greedy for this.
        [1,5] [1,4] [2,8]x [3,4]x [3,5]x
        """
        if not intervals: return 0
        intervals.sort(key=lambda x: x.start) # sort on start time
        # avoid making new array
        """
        # trick with iters
        intervals = iter(intervals) # iter trick
        current_end, count = next(intervals).end, 0 
        """
        current_end, count = intervals[0].end, 0
        for index in range(1, len(intervals)):
            interval = intervals[index]
            if interval.start < current_end:  # find overlapping interval
                # case 1: [1,2] [1,3]
                count += 1
                # greedy here
                current_end = min(current_end, interval.end)  # erase the one with larger end time
            else:
                # case 1: [1,2] [2,3] 
                # case 2: [1,2] [3,4]
                current_end = interval.end   # update end time
        return count
