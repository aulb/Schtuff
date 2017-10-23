class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sorted array
        start = 0
        prev = None
        for index in range(len(nums)):
            # If its not the same, switch
            if nums[index] != prev:
                # Capture previous/unique
                prev = nums[index]
                
                # Swap and increment counter
                nums[index], nums[start] = nums[start], nums[index]
                start += 1
                
        return start
