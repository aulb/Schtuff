import heapq
import sys

class Stream:
    def __init__(self):
        self.data = []

    def add(self, element):
        self.data.append(element)

    def pop(self):
        return None if self.empty() else self.data.pop(0)

    def peek(self):
        return None if self.empty() else self.data[0]

    def empty(self):
        return len(self.data) == 0

class StreamElement:
    def __init__(self, element, which_stream):
        self.element = element
        self.which_stream = which_stream
    
    def __cmp__(self, other):
        return cmp(self.element, other.element)

"""
>>> heapq.heappush(q, MyObject(50))
>>> heapq.heappush(q, MyObject(40))
>>> heapq.heappush(q, MyObject(30))
>>> heapq.heappush(q, MyObject(20))
>>> heapq.heappush(q, MyObject(200))
"""

# Runtime analysis:
# Total amount of streams = k
# length of longest stream = n
# building the initial heap = klogk
# reheapifying = logk
# we are reheapifying is n times
# O(max(n, k)logk)
def get_stream_sorted_order(streams):
    result = []
    # We need to put all of the streams into the min heap
    # Nodes of the heap will be the first element in the stream
    
    # Initializing the min heap
    min_heap = []
    for index, stream in enumerate(streams):
        element = stream.pop() if not stream.empty() else -sys.maxsize # Minimum number in Python possible
        heapq.heappush(min_heap, StreamElement(element, index))
       
    # Popping from min heap and replenish the result array
    """>>> obj = heapq.heappop(q)"""
    # Assume that no integer in the stream is the minimum number possible
    stream_element = heapq.heappop(min_heap) # Gives me the StreamElement
    # Check if the stream_element is equal to the minimum number, then we are done
    while stream_element.element != -sys.maxsize:
        # Append the element, and then replenish
        result.append(stream_element.element)

        # Find out which element it comes from
        which_stream = stream_element.which_stream
        element = streams[which_stream].pop() if not streams[which_stream].empty() else -sys.maxsize # Minimum number in Python possible
        
        heapq.heappush(min_heap, StreamElement(element, index))
        heapq.heapify(min_heap)
        
        # Get the next stream_element
        stream_element = heapq.heappop(min_heap)
    
    return result
 
def get_stream_column_order(streams):
    result = []
    # This is like "visited", to check if a stream is empty
    is_stream_empty = [False] * len(streams)
    total_empty_streams = 0
    stream_counter = 0
    
    # Total amount of streams = k
    # length of longest stream = n
    # O(nk)
    while is_empty < len(streams):
        # If stream is empty then do nothing and 
        if streams[stream_counter].empty():
            if not is_stream_empty[stream_counter]: 
                total_empty_streams += 1 # total_empty_streams = 2
                is_stream_empty[stream_counter] = True # [True, True]
        else:
            # Append result
            result.append(streams[stream_counter].pop())
        
        # Reset the counter or add
        if stream_counter == len(streams) - 1: stream_counter = 0
        else: stream_counter += 1
    # result = [1, 2, 8, 5, 12, 6, 9]
    return result

# Example 1
# Stream 1:  1, 8, 12
# Stream 2:  2, 5, 6,  9,
# Output: 1, 2, 8, 5, 12, 6, 9

# Output: 1, 2, 5, 6, 8, 9, 12

# Stream 3:  3, 7, 10, 14, 20  
# Output: 1, 2, 3, 8, 5, 7, 12, 6, 10, 9, 14, 20 

# Example 2
# Stream 1: null
# Stream 2: 1, 8, 12
# Stream 3: 2, 3, 5
# Output: 1, 2, 8, 3, 12, 5
