def heapify(array):
	# Iterate backwards from the non leaves
	for index in range((len(array) - 1) // 2, -1, -1):
		max_heapify(array, index)
	return array


def max_heapify(array, index):
	left = 2 * index + 1
	right = 2 * index + 2

	largest = index
	# Need to check "heapsize" to make sure left and right are still in the boundary
	if (left < len(array) and array[left] > array[largest]): largest = left
	if (right < len(array) and array[right] > array[largest]): largest = right

	if (largest != index): 
		# Swap
		array[index], array[largest] = array[largest], array[index]
		max_heapify(array, largest)

if __name__ == '__main__':
	unheaped_1 = [9,6,5,0,8,2,7,1,3]
	heaped_1 = [9,8,7,3,6,2,5,1,0]

	unheaped_2 = [10,9,8,7,6,5,4,3,2,1]
	heaped_2 = unheaped_2

	unheaped_3 = list(range(10))
	heaped_3 = [9,8,6,7,4,5,2,0,3,1]

	assert heapify(unheaped_1) == heaped_1
	assert heapify(unheaped_2) == heaped_2
	assert heapify(unheaped_3) == heaped_3
