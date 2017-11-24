import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.internal_size = 0
        # Min heap holds the greater half of nums, max heap holds the lesser half of nums
        self.min_heap, self.max_heap = [], []


    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        """heapq.heappushpop(heap, item)¶
        Push item on the heap, then pop and return the smallest item from the heap. 
        The combined action runs more efficiently than heappush() followed by a separate call to heappop().
        """
        # If the internal size is odd, add to max, pop, add to min
        if self.internal_size & 1: 
            # Trick with heapq max heap is to just multiply the number by -1
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
        # If the internal size is even, add to max
        else:
            heapq.heappush(self.max_heap, -num)
            if self.min_heap and -self.max_heap[0] > self.min_heap[0]:
                # Swap
                minimum, maximum = heapq.heappop(self.min_heap), -heapq.heappop(self.max_heap)
                
                # Push the values to the other heap
                heapq.heappush(self.min_heap, maximum)
                heapq.heappush(self.max_heap, -minimum)
                
        # Don't forget to increment the size on every addition
        self.internal_size += 1
        
        
    def findMedian(self):
        """
        :rtype: float
        """
        # The key is to pick from one heap, one heap is always the "pivot" or "anchor"
        # I choose max heap to be it

        # If empty...
        if not self.internal_size: return 0.0
        
        # If the internal size is odd, get median from the max
        elif self.internal_size & 1: return -self.max_heap[0]
        # If the internal size is even, get median from the min and max heap divided by 2
        else: return (self.min_heap[0] - self.max_heap[0]) / 2.0
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
