# Use a "stack" to keep track of the earliest immediate price that is greater than current
def calculate_span(stocks):
	stack = []
	spans = []

	for index, price in enumerate(stocks):
		# stock price for the index at the top of the stack
		while len(stack) > 0 and stocks[stack[len(stack) - 1]] <= price:
			# if the top is still greater, then pop, or if its empty
			stack.pop() # last item gone

		empty_stack = len(stack) == 0
		spans.append(1 if empty_stack else index - stack[len(stack) - 1])
		stack.append(index)
	return spans

if __name__ == '__main__':
	array = [100, 80, 60, 70, 60, 75, 85]
