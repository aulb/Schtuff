# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
"""
What we care about is the start <= old.end, merge
Old solution: take one, compare with the rest, with index tracking so we don't double back
New solution: just use the result array to merge

"""
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        for interval in sorted(intervals, key = lambda interval: interval.start):
            if result and result[-1].end >= interval.start: 
                result[-1].end = max(interval.end, result[-1].end)
            else: result.append(interval)
        return result   
#         # Not really sorted??? sorted by end I think
#         i, n = 0, len(intervals)
#         result = []
#         intervals = sorted(intervals, key = lambda i: i.start) 
#         while i <= n - 1:
#             start, end = intervals[i].start, intervals[i].end
#             while i < n - 1:
#                 next_start, next_end = intervals[i + 1].start, intervals[i + 1].end
                
#                 # Merge if the current end and the last end is the same or greater than the next start
#                 # (1,3), (2,4) => (1,4)
#                 if end >= next_start:
#                     if start >= next_start:
#                         start = min(start, next_start)
#                     end = max(end, next_end)
#                     i += 1
#                 else:
#                     break

#             # Append the current result
#             result.append(Interval(start, end)) 
#             # Advance the counter
#             i += 1
            
#         # How to merge the last one in?
#         return result

# """
# def merge(self, intervals): # sort first
#     out = []
#     for i in sorted(intervals, key=lambda i: i.start):
#         if out and i.start <= out[-1].end:
#             out[-1].end = max(out[-1].end, i.end)
#         else:
#             out += i,
#     return out
# """
