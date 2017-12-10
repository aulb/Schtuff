# Offline median
from collections import defaultdict
from heapq import heapify, heappush, heappop, heappushpop
class Solution:
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        """
        Goal#1: Every iteration we need the heaps to be "balanced"
        References:
            1) Heap balances
            Heap balance lesser than 0 means that there are "more element" in the max heap, transfer one over to the min heap
            Heap balance greater than 0 means more element in the min heap, transfer one over to the max heap
        """
        # k needs to be greater than 0, nums needs to not be empty
        # assumed all integers, duplicates allowed
        if not nums or not k: return []
        to_be_deleted, result = defaultdict(int), []
        # min_heap stores the larger half, max_heap stores the smaller half 
        min_heap, max_heap = nums[:k], []
        heapify(min_heap) # do this so it doesn't affect the original array
    
        # transfer half the content to max_heap
        # max heap is guaranteed to have something when k > 1
        while len(min_heap) - len(max_heap) > 1:
            heappush(max_heap, -heappop(min_heap))
        
        for index in range(k, len(nums) + 1):
            # print(min_heap, max_heap)
            # add median to result
            if k & 1: result.append(float(min_heap[0]))
            else: result.append((min_heap[0] - max_heap[0]) / 2)

            # done here
            if index >= len(nums): break
            
            # rebalancing starts here, refer to goal#1
            # becareful when assigning the incoming and outgoing numbers
            incoming_num, outgoing_num = nums[index], nums[index - k]
            heap_balance = 0
            # print(incoming_num, outgoing_num)
            
            # remove outgoing element, 
            # if the outgoing num is geq than the top of min heap, (that num) exist in the min heap
            # min heap is always there
            if outgoing_num >= min_heap[0]:
                heap_balance -= 1
                # outgoing_num is the top element of min_heap
                if outgoing_num == min_heap[0]: heappop(min_heap)
                # if nothing was deleted, save number to delete later (stage deletion)
                else: to_be_deleted[outgoing_num] += 1
            # outgoing num is lesser than top of min heap, that num exists in the max heap
            else:
                # make sure max_heap is not empty
                heap_balance += 1
                if outgoing_num == -max_heap[0]: heappop(max_heap)
                else: to_be_deleted[outgoing_num] += 1
            # print(min_heap, max_heap, heap_balance)
            
            # add incoming element
            # min_heap might be empty in cases such as k = 1, in that case always add to min_heap no matter what
            if not min_heap or incoming_num >= min_heap[0]:
                # incoming element is geq min_heap
                # add to MAX HEAP FIRST, then to min heap
                heappush(min_heap, -heappushpop(max_heap, -incoming_num))
                heap_balance += 1
            else:
                heappush(max_heap, -incoming_num)
                heap_balance -= 1
            # print(min_heap, max_heap, heap_balance)
            
            # rebalance the heaps
            # need to add to the min heap
            if heap_balance < 0: heappush(min_heap, -heappop(max_heap))
            # need to add to the max heap
            elif heap_balance > 0: heappush(max_heap, -heappop(min_heap))
                
            # delete staged numbers, DECREMENT FIRST, then pop
            while min_heap and to_be_deleted[min_heap[0]]:
                to_be_deleted[min_heap[0]] -= 1
                heappop(min_heap)
            # notice -max_heap[0] because we store negative nums in max heap
            while max_heap and to_be_deleted[-max_heap[0]]:
                to_be_deleted[-max_heap[0]] -= 1
                heappop(max_heap)
            
            # print(min_heap, max_heap)
            # print()
        return result
