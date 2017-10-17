# March 2017
# Keep order, swapping works if we wanna keep the order
# Bubble sort works but n^2, also another requirement: in place

# Naive: copy to new array: O(n) time and space

# Do one with swapping: O(n) time constant space


# Another without swapping ? stacks? not in place 
# Pop and put into stack NO NO NO, the solution below is in place
class Solution(object):
	def moveZeroes(self, nums):
		start = 0
		for i in range(len(nums)):
			if nums[i] != 0:
				# Swap with the lagged pointer
				nums[i], nums[start] = nums[start], nums[i]
				start += 1
