# Not really in place
def merge(array, start, middle, end):
	# Need to exhaust all elements here
	left = array[start:middle] # Create two temporary arrays
	right = array[middle:end]
	i, j = 0, 0

	# Iterate from start to end, if one counter hits the end, do the other one
	for k in range(start, end):
		if i == len(left):
			array[k] = right[j]
			j += 1
		elif j == len(right):
			array[k] = left[i]
			i += 1
		elif left[i] < right[j]:
			array[k] = left[i]
			i += 1
		else:
			array[k] = right[j]
			j += 1


def merge_in_place(array, start, middle, end): # NO
	# Need to exhaust all elements here
	i, j = start, middle
	print(array[start:middle])
	print(array[middle:end])
	print()
	print(i, j)
	print(start, middle, end)
	print()
	# Iterate from start to end, if one counter hits the end, do the other one
	for k in range(start, end):
		print(i, j)
		if i == middle and j != end:
			array[k], array[j] = array[j], array[k]
			j += 1
		elif j == end and i != middle:
			array[k], array[i] = array[i], array[k]
			i += 1
		elif array[i] < array[j]:
			array[k], array[i] = array[i], array[k]
			i += 1
		else:
			array[k], array[j] = array[j], array[k]
			j += 1
	print(k, i, j)



def merge_sort(array, start, end):
	# Need at least [0:2] for it to do something, otherwise skip
	if end - start <= 1:
		return

	middle = (start + end) // 2
	merge_sort(array, start, middle)
	merge_sort(array, middle, end)
	merge(array, start, middle, end)


def merge_sort_in(array, start, end):
	# Need at least [0:2] for it to do something, otherwise skip
	if end - start <= 1:
		return

	middle = (start + end) // 2
	merge_sort(array, start, middle)
	merge_sort(array, middle, end)
	merge_in_place(array, start, middle, end)


if __name__ == '__main__':
	# array = [45,-1,0,133,2]
	# merge_sort(array, 0, len(array))
	# print(array)

	array = [45,-1,0,133,2]
	merge_sort_in(array, 0, len(array))
	print(array)
