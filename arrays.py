from collections import Counter
def count_distinct_window(array, window_size):
	# O(n) time
	# O(n) space
	if window_size < 1:
		return []

	# If window size is bigger...
	if window_size > len(array):
		return []

	# Assumed window size ...
	result = []
	counter = Counter()

	# initialization
	count_distinct = 0
	for i in range(window_size):
		current_number = array[i]
		current_count = counter.get(current_number, 0)
		if current_count == 0:
			count_distinct += 1
		counter[current_number] = current_count + 1
	result.append(count_distinct)

	# moving window
	for i in range(window_size, len(array)):
		current_number = array[i]
		previous_number = array[i - window_size] # beginning of array, not previous
		current_count = counter.get(current_number, 0)
		previous_count = counter.get(previous_number) # must be one from before
		# If its the last one that means its about to get "popped off" the hash
		if previous_count == 1:
			count_distinct -= 1
		# Incoming number is a distinct
		if current_count == 0:
			count_distinct += 1
		counter[current_number] = current_count + 1
		counter[previous_number] = previous_count - 1
		result.append(count_distinct)

	return result

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


# geeks for geeks walkthrough
def get_largest_product(array):
	# always a positive number!
	# 0 boundaries
	# negative numbers
	n = len(array)

	# temporary values
	max_ending_here = 1
	min_ending_here = 1 # keep track of the "latest negative in a sense"

	# maximum value
	maximum = 1

	for i in range(n):
		# Positive element, the easiest case
		# Keep track of positive and negative
		if array[i] > 0:
			max_ending_here = max_ending_here * array[i]
			min_ending_here = min(min_ending_here * array[i], 1) # Keep track of minimum
		# Reset, another easy case
		elif array[i] == 0:
			max_ending_here = 1
			min_ending_here = 1
		# Negative element...
		# max ending - 1 or positive
		# min ending - 1 or negative
	else:
		temp = max_ending_here
		max_ending_here = max(min_ending_here * array[i], 1)
		min_ending_here = temp * array[i]

	if maximum < max_ending_here:
		maximum = max_ending_here
	return maximum
		
def get_largest_sum(array):
	prev = maximum = array[0]
	for number in array:
		prev = number + (prev if prev > 0 else 0)
		if prev > maximum:
			maximum = prev
	return maximum

if __name__ == '__main__':
	unique_window1 = [1,1,1,2,1,3]
	result_window1 = [2,2,3]
	unique_window2 = [2,1,3,4,1,3,4]
	result_window2 = [4,3]

	assert count_distinct_window(unique_window1,4) == result_window1
	assert count_distinct_window(unique_window2,6) == result_window2

	largest1 = [-1,2,3] # 6
	largest2 = [-1,2,3,-1] # 6
	largest3 = [1,2,0,2,6] # 12
	largest4 = [-1,5,0,2,1,2] # 5
