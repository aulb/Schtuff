# There are n1 steps to get to n - 1
# There are n2 steps to get to n - 2
# To make n steps there are n1 + n2 ways
# From n1 make one step to get to n
# From n2 make two steps (not one step and another because it'll overlap with the steps in n1) to get to n

def climb_stairs(n):
	if n <= 0: return 0 # one way, don't make a move
	if n == 1: return 1 # one way, make one step
	if n == 2: return 2 # make 2 one steps, or 1 two step

	# Fib iterate
	a = 1
	b = 2
	c = 0

	for i in range(2, n):
		c = a + b
		a = b
		b = c
	return c


# Fib recurse
def fib_rec(n):
	if n <= 0: return 0 
	if n == 1: return 1 
	if n == 2: return 2

	return fib_rec(n - 1) + fib_rec(n - 2)
