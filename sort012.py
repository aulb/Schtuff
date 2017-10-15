def sort012(array):
	a = [0,1,1,2,1,0]
	# have pointers to tell where to switch and all
	# once you switch with low, its done, fixed
	low = 0
	high = len(array) - 1
	mid = 0

	# middle is the fast pointer
	while mid <= high:
		if array[mid] == 0:
			a[low], a[mid] = a[mid], a[low]
			low += 1
			mid += 1
		elif a[mid] == 1:
			mid += 1
		else: # a[mid] == 2
			a[mid], a[high] = a[high], a[mid]
			high -= 1
	return array

if __name__ == '__main__':
	pass
