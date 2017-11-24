# // Given a list of integers of length n+1, with values between 1 and n,
# // return a number in that list that appears more than once.

# // Example:
# // [1, 2, 1, 3]         —>    return 1
# // [4, 1, 2, 3, 3, 1]   —>    return 3 or 1

# [6, 3, 2, 1, 4, 5, 5]
# (1, 2, 3) (4, 5, 5, 6)
def find_duplicates_unique(array): # linear time, constant space
	# Guaranteed between 1 to n, size is n + 1 so the last index is n
	for i in range(0, len(array)):
		# Get the current number, which is also an index to visit
		index_to_visit = abs(array[i]) # also an index
		
		# If visited the value will be negative
		if array[index_to_visit] < 0:
			return index_to_visit
		# Otherwise make negative
		array[index_to_visit] *= -1

	return -1 # No index is duplicated?
