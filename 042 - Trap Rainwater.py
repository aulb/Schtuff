# Linear time, linear space
def find_water(array):
	left, right = [], []
	result = 0
	left[0] = array[0]
	for i in range(1, len(array)):
		# find the tallest on the left
		left[i] = max(left[i - 1], array[i])

	for i in range(len(array) - 2, 0, -1):
		right[i] = max(right[i + 1], array[i])

	for i in range(len(array)):
		result + min(left[i], right[i]) - array[i]

	return result

def find_water_optimized(array):
	# TODO
	pass
