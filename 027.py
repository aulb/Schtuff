# https://stackoverflow.com/questions/135041/should-you-always-favor-xrange-over-range
# In place
# Shuffle around doesn't work because you don't exactly know where to shuffle to
def removeElement(nums, val):
	for i in range(len(nums) - 1, -1, -1):
		# Strategies:
		# Iterate backwards
		if nums[i] == val:
			del nums[i]
	return len(nums)
