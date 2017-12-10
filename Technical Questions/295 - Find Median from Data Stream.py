"""
Goal: 
- always want the max heap to have more element than the min heap
- adding number to max heap first, then immediately add to min heap
    - this way we are guaranteed to always have the greater half to be on the min heap
    - if we accidentally add too much to min heap, just simply pop the min heap and transfer over to the max heap
"""
# Better implementation
from heapq import *
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # small, large => min_heap, max_heap
        # small/min_heap contains the largest half of all the elements
        # large/max_heap contains the smallest half of all the elements
        self.heaps = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        # Want max_heap to always have more element
        min_heap, max_heap = self.heaps
        
        """
        # push to max_heap
        heappush(max_heap, -num)
        
        # pop from max_heap
        greatest_from_max_heap = -heappop(max_heap)

        # push to min_heap
        heappush(min_heap, greatest_from_max_heap)

        if len(min_heap) > len(max_heap):
            # get the lowest value from min heap
            lowest_from_min_heap = heappop(min_heap)
            
            # push to max heap
            heappush(max_heap, -lowest_from_min_heap)
        """

        heappush(min_heap, -heappushpop(max_heap, -num))
        if len(min_heap) > len(max_heap):
            heappush(max_heap, -heappop(min_heap))
        

    def findMedian(self):
        """
        :rtype: float
        """
        min_heap, max_heap = self.heaps
        if not max_heap: return 0.0
        if len(max_heap) > len(min_heap): return float(-max_heap[0])
        return (-max_heap[0] + min_heap[0]) / 2

# import heapq
# class MedianFinder:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.internal_size = 0
#         # Min heap holds the greater half of nums, max heap holds the lesser half of nums
#         self.min_heap, self.max_heap = [], []


#     def addNum(self, num):
#         """
#         :type num: int
#         :rtype: void
#         """
#         """heapq.heappushpop(heap, item)¶
#         Push item on the heap, then pop and return the smallest item from the heap. 
#         The combined action runs more efficiently than heappush() followed by a separate call to heappop().
#         """
#         # If the internal size is odd, add to max, pop, add to min
#         if self.internal_size & 1: 
#             # Trick with heapq max heap is to just multiply the number by -1
#             heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
#         # If the internal size is even, add to max
#         else:
#             heapq.heappush(self.max_heap, -num)
#             if self.min_heap and -self.max_heap[0] > self.min_heap[0]:
#                 # Swap
#                 minimum, maximum = heapq.heappop(self.min_heap), -heapq.heappop(self.max_heap)
                
#                 # Push the values to the other heap
#                 heapq.heappush(self.min_heap, maximum)
#                 heapq.heappush(self.max_heap, -minimum)
                
#         # Don't forget to increment the size on every addition
#         self.internal_size += 1
        
        
#     def findMedian(self):
#         """
#         :rtype: float
#         """
#         # The key is to pick from one heap, one heap is always the "pivot" or "anchor"
#         # I choose max heap to be it

#         # If empty...
#         if not self.internal_size: return 0.0
        
#         # If the internal size is odd, get median from the max
#         elif self.internal_size & 1: return -self.max_heap[0]
#         # If the internal size is even, get median from the min and max heap divided by 2
#         else: return (self.min_heap[0] - self.max_heap[0]) / 2.0
            


# # Your MedianFinder object will be instantiated and called as such:
# # obj = MedianFinder()
# # obj.addNum(num)
# # param_2 = obj.findMedian()
