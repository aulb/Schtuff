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

if __name__ == '__main__':
	largest1 = [-1,2,3] # 6
	largest2 = [-1,2,3,-1] # 6
	largest3 = [1,2,0,2,6] # 12
	largest4 = [-1,5,0,2,1,2] # 5
