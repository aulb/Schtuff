# array is guaranteed unique
def selection_sort(array):
	if not array: return array
	start = index = 0

	while start < len(array):
		# Reinitialize minimums
		index = minimum_index = start
		while index < len(array):
			if array[minimum_index] > array[index]:
				minimum_index = index			
			index += 1
		# Swap
		array[start], array[minimum_index] = array[minimum_index], array[start]
		# Advance start
		start += 1

	return array

if __name__ == '__main__':
	array = [2,7,4,1,5,3,9,9]
	print(selection_sort(array))
