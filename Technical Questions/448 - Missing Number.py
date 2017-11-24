class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * len(nums) # [0, 0]
        for num in nums:
            result[num - 1] = num
        
        start = 0
        for index, num in enumerate(result):
            if num is 0:
                result[start] = index + 1
                start += 1
        
        return result[:start]
