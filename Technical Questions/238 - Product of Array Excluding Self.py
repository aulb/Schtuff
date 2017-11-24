class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prev = 1
        result = [1] * len(nums)
        # Left calculate
        for index, num in enumerate(nums):
            result[index] *= prev
            prev *= num
        
        prev = 1
        for index in range(len(nums) - 1, -1, -1):
            result[index] *= prev
            prev *= nums[index]
        
        return result
