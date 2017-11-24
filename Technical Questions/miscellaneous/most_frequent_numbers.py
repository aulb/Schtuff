from collections import Counter

def modified_heapify(array):
	# Iterate backwards from the non leaves
	for index in range((len(array) - 1) // 2, -1, -1):
		min_modified_heapify(array, index)
	return array


def min_modified_heapify(array, index):
	left = 2 * index + 1
	right = 2 * index + 2

	smallest = index
	# Need to check "heapsize" to make sure left and right are still in the boundary
	if (left < len(array) and array[left][1] < array[smallest][1]): smallest = left
	if (right < len(array) and array[right][1] < array[smallest][1]): smallest = right

	# no need to modify the heap if the smallest thing is the same as index, means it sorted
	if (smallest != index): 
		# Swap
		array[index], array[smallest] = array[smallest], array[index]
		min_modified_heapify(array, smallest)

# Use a min heap, similar to "kth" smallest number
def most_frequent_numbers(array, k):
	counter = Counter()

	for number in array:
		current_count = counter.get(number, 0)
		counter[number] = current_count + 1

	counter = list(counter.items()) # This operation is O(n)

	# make min heap of size k now
	heapified = modified_heapify(counter[:k])
	for i in range(k, len(counter)):
		if heapified[0][1] < counter[i][1]:
			# swap
			heapified[0] = counter[i]
			heapified = modified_heapify(heapified)

	return heapified

if __name__ == '__main__':
	array = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9]
	heapified = most_frequent_numbers(array, 4)
