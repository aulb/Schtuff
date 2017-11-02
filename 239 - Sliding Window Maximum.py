from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k < 1: return [] # Technically we don't even need this because line 29 takes care of it
        # Queue pop, popleft, append are all amortized O(1)
        # Average case of also O(1)
        queue = deque()
        result = []
        # Iterate through 
        for index, num in enumerate(nums):
            # Always check if queue is not empty then access the index
            while queue and nums[queue[-1]] < num:
                queue.pop() # Pop the right end
            
            # Append to the end of the queue
            queue.append(index)
            
            # If the first element in the array (the index) is outside the sliding window range, dequeue it
            if queue[0] == index - k: queue.popleft()
            
            # At the end we check and append, queue[0] will always have the greatest element
            # We cannot simply do result.append because we need to make sure its in the sliding window first
            # k - 1 because zero indexing
            if index >= k - 1: result.append(nums[queue[0]])
                
        return result
