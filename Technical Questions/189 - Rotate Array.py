class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # Make sure its within n
        # k = k % n

        # # Simultaneous assignment
        nums[:k], nums[k:] = nums[n - k:], nums[:n - k]
        # left = nums[:n - k]
        # right = nums[n - k:]
        
        # for i in range(n):
        #     nums[i] = right[i] if i < k else left[i - k]
