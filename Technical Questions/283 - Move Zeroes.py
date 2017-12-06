# March 2017
# Keep order, swapping works if we wanna keep the order
# Bubble sort works but n^2, also another requirement: in place

# Naive: copy to new array: O(n) time and space

# Do one with swapping: O(n) time constant space


# Another without swapping ? stacks? not in place 
# Pop and put into stack NO NO NO, the solution below is in place
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start = 0
        for i in range(len(nums)):
            # Only swap when there is a non zero, increment the "zero" counter every swap
            # swap with the lagged pointer
            if nums[i]:
                nums[i], nums[start] = nums[start], nums[i]
                start += 1
