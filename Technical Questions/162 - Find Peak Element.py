class Solution:
    def isPeak(self, nums, index):
        if ((index - 1 >= 0 and nums[index - 1] < nums[index]) or (index - 1 < 0)) and ((index + 1 <= len(nums) - 1 and nums[index + 1] < nums[index]) or (index + 1 > len(nums) - 1)): 
            return True
        return False
    
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums)
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.isPeak(nums, mid): return mid
            # Go to the right if the greater element is on the right
            if mid - 1 < 0 or (mid + 1 <= len(nums) - 1 and nums[mid + 1] > nums[mid]):
                lo = mid + 1
            else:
                hi = mid - 1
