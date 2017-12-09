class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        stack = []
        start, end = len(nums), 0
        max_so_far = nums[0]
        for index, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                start = min(start, stack.pop())
                end = index + 1
            if max_so_far > num: 
                end = index + 1
            else:
                max_so_far = num
            stack.append(index)
        
        return max(end - start, 0)
