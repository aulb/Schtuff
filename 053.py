class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = max = nums[0]
        for n in nums[1:]:
            prev = n + (prev if prev > 0 else 0)
            if max < prev:
                max = prev
        return max