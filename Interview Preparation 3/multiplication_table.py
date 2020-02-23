def pad_string(string, max_length):
	return string + (max_length - len(string)) * ' '

def print_multiplication_table(a, b):
	if not (a and b): return

	max_length = len(str(a * b))
	for i in range(1, a + 1):
		current_line = ''
		for j in range(1, b + 1):
			current_line += '{} '.format(pad_string(str(i * j), max_length))

		print(current_line)

if __name__ == '__main__':
	print_multiplication_table(12, 12)
