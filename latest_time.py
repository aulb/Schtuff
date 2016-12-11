# Last Modified: ??
# Given 4 numbers, print out the latest time that is arrangable!
# Example: [1,2,3,4] -> '23:41'
def minutes(A):
	first_index = A.index(max(A))
	first = A.pop(first_index)
	second = A.pop()

	if first > 5:
		if second > 5:
			# Impossible
			return [-1,0]
		# Otherwise
		return [second, first]
	else:
		return [first, second]

def late(A):
	A_ = A[:]

	# Find main hour
	for i in range(3)[::-1]:
		if i in A:
			# Find second hour
			main_hour_index = A.index(i)
			main_hour = A.pop(main_hour_index)			
			x = 10 if i is not 2 else 4
			for j in range(x)[::-1]:
				if j in A:
					second_hour_index = A.index(j)
					second_hour = A.pop(second_hour_index)
					# Find minutes now
					minute = minutes(A)

					latest = [main_hour, second_hour]
					if sum(minute) is not -1:
						latest.extend(minute)
						return latest
		# Copy back
		A = A_[:]

	# Trippin
	return [0,0,0,0]

if __name__ == '__main__':
	print late([1,3,9,6])
	print late([1,2,3,4])
	print late([2,0,9,9])
	print late([9,9,9,9])