class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = max = nums[0]
        for n in nums[1:]:
            # Only accept prev if its more than 0, otherwise no
            prev = n + (prev if prev > 0 else 0)
            if max < prev:
                # If prev is bigger then set max as prev
                max = prev
        return max
