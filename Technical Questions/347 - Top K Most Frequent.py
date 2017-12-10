# Top most frequent offline
from collections import Counter
# class Solution:
#     def topKFrequent(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         if not nums: return []
#         # At most k
#         bucket = [None for _ in range(len(nums) + 1)]
#         result = []
#         counts = Counter(nums)
        
#         for element in counts:
#             count = counts[element]
#             if not bucket[count]:
#                 bucket[count] = [element]
#             else:
#                 bucket[count].append(element)
                
#         counter = 0
#         for index in range(len(nums), -1, -1):
#             if bucket[index]:
#                 result.extend(bucket[index])
#                 counter += 1
#             if counter == k: return result
#         # not enough k or just barely made it
#         return result

# Runtime
# n : number of elements in nums
# making counts -> linear
# making buckets -> linear
# iterate buckets -> linear
# O(n)
def top_k_elements(nums, k):
    if not nums: return []
    result = []
    counts = Counter(nums)

    # Can save on memory if we count first, and then find the maximum and build the bucket that way
    # Create bucket now
    bucket_size = max(counts.values())
    bucket = [None for _ in range(bucket_size + 1)]
    
    for element in counts:
        count = counts[element]
        if not bucket[count]:
            bucket[count] = [element]
        else:
            bucket[count].append(element)

    counter = 0
    for index in range(len(bucket) -1, -1, -1):
        if not bucket[index]: continue
        for element in bucket[index]:
            result.append(element)
            counter += 1
            if counter == k: return result
    # not enough k or just barely made it
    return result

if __name__ == '__main__':
    print(top_k_elements([], 10))
    print(top_k_elements([2,1,3,3,3,4,4,5,5,5,5,5], 10))
