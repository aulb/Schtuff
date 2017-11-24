def heapify(array):
	# Iterate backwards from the non leaves
	for index in range((len(array) - 1) // 2, -1, -1):
		min_heapify(array, index)
	return array


def min_heapify(array, index):
	left = 2 * index + 1
	right = 2 * index + 2

	smallest = index
	# Need to check "heapsize" to make sure left and right are still in the boundary
	if (left < len(array) and array[left] < array[smallest]): smallest = left
	if (right < len(array) and array[right] < array[smallest]): smallest = right

	if (smallest != index): 
		# Swap
		array[index], array[smallest] = array[smallest], array[index]
		min_heapify(array, smallest)

def get_k_largest_element(array, k, sort=False):
	if k < 1:
		return []

	# if k is bigger than length of array, wtf then
	if k >= len(array):
		return array

	# build min heap of size k
	k_heapified_array = heapify(array[:k])

	# for each of the remaining elements
	for i in range(k, len(array)):
		# if the top element is lesser than array[k], then replace
		if k_heapified_array[0] < array[i]:
			k_heapified_array[0] = array[i]
			# heapify array again
			heapify(k_heapified_array)

	if sort: k_heapified_array.sort()
	return k_heapified_array

if __name__ == '__main__':
	array1 = [1,2,3,4,5,6,7,8,9]
	array2 = [1,3,5,2,1,0,10,9,7,9,8,9,2]

	assert get_k_largest_element(array1, 3) == [7,8,9]
	assert get_k_largest_element(array1, 100) == [1,2,3,4,5,6,7,8,9]
	assert get_k_largest_element(array1, -1) == []
	assert get_k_largest_element(array2, 3, True) == [9,9,10]
