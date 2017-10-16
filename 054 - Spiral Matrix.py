def spiral_print(matrix):
	result = []
	row, col = len(matrix), len(matrix[0])
	iter_max = row * col
	counter = 0

	row_start, row_end = 0, row - 1
	col_start, col_end = 0, col - 1

	while counter < iter_max:
		# Do forward
		for j in range(col_start, col_end + 1):
			# Fix row
			result.append(matrix[row_start][j])
			print('first', matrix[row_start][j])
			counter += 1
		# Done with this row, increment it
		row_start += 1

		# Do downward
		for i in range(row_start, row_end + 1):
			# Fix column
			result.append(matrix[i][col_end])
			print('second', matrix[i][col_end])
			counter += 1
		# Done with this column, decrement it
		col_end -= 1

		# Do backward TODO investigate
		if counter >= iter_max: break
		for j in range(col_end, col_start - 1, -1):
			# Fix row
			result.append(matrix[row_end][j])
			print('third', matrix[row_end][j])
			counter += 1
		# Done with this row, decrement it
		row_end -= 1

		# Do upward
		if counter >= iter_max: break
		for i in range(row_end, row_start - 1, -1):
			# Fix column
			result.append(matrix[i][col_start])
			print('fourth', matrix[i][col_start])
			counter += 1
		col_start += 1


	return result

if __name__ == '__main__':
	array = [
		[ 1, 2, 3, 4, 5 ],
		[ 1, 2, 3, 4, 5 ],
		[ 1, 2, 3, 4, 5 ],
		[ 1, 2, 3, 4, 5 ]
	]

	print(spiral_print(array))
