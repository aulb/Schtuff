#!/usr/bin/env python
from fractions import gcd

def lcm(a, b):
	return (a * b) // gcd(a, b)

# <strike>Fizzbuzz</strike> Cracklepop with more crackle popping.
def fizzbuzz(numlist, crackle, pop):
	cracklepop = lcm(crackle, pop)
	for n in numlist:
		if not n % cracklepop:
			print 'CracklePop'
		elif not n % crackle:
			print 'Crackle'
		elif not n % pop:
			print 'Pop'
		else:
			print n

if __name__ == '__main__':
	crackle = 3
	pop = 5
	numlist = range(1, 101)

	# I just realized after writing this that 
	# there is more than lcm and divisibility
	# properties than cracklepops
	fizzbuzz(numlist, crackle, pop)