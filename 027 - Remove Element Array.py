# https://stackoverflow.com/questions/135041/should-you-always-favor-xrange-over-range
# In place
# Shuffle around doesn't work because you don't exactly know where to shuffle to
# def removeElement(nums, val):
# 	for i in range(len(nums) - 1, -1, -1):
# 		# Strategies:
# 		# Iterate backwards
# 		if nums[i] == val:
# 			del nums[i]
# 	return len(nums)
# DELETING DOES NOT WORK, NOT O(n) OPERATION

def removeElement(nums, val):
	start = 0
	for i in range(len(nums)):
		if nums[i] != val:
			nums[i], nums[start] = nums[start], nums[i]
			start += 1
	return nums[:start]
