# Use a "stack" to keep track of the earliest immediate price that is greater than current
def calculate_span(stocks):
	stack, spans = [], []

	for index, price in enumerate(stocks):
		# stock price for the index at the top of the stack
		# if the top is still greater, then pop, or if its empty
		# last item gone
		while stack and stocks[stack[-1]] <= price: stack.pop()
		spans.append(1 if not stack else index - stack[-1])
		stack.append(index)

	return spans

if __name__ == '__main__':
	array = [100, 80, 60, 70, 60, 75, 85]
	print(calculate_span(array))
